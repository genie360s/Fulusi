import requests
import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

latest_trading_date_url = os.getenv("LATEST_TRADING_DATE")
indices_api_url = os.getenv("DSE_INDICES_API_URL")

# API request to get the latest trading date
response_date = requests.get(latest_trading_date_url)

# Check if the request was successful
if response_date.status_code == 200:
    data = response_date.json()
    latest_date = data['data']
    print(latest_date)
else:
    print("Error: Could not retrieve data from the API")
    print(response_date.text)
    exit()

# API request to get the indices
response_indices = requests.get(f"{indices_api_url}{latest_date}")
print(response_indices)

# Check if the request was successful
if response_indices.status_code == 200:
    data = response_indices.json()
    indices_data = data['data']
else:
    print("Error: Could not retrieve data from the API")
    exit()

# Connect to the PostgreSQL database
try:
    connection = psycopg.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME")
    )
    cursor = connection.cursor()
except Exception as e:
    print("Error: Could not connect to the database")
    print(e)
    exit()

# Check if the table exists, if not create it
def check_and_create_table(cursor):
    table_check_query = """
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public'
            AND table_name = 'dse_indices'
        );
    """
    cursor.execute(table_check_query)
    table_exists = cursor.fetchone()[0]

    if not table_exists:
        create_table_query = """
            CREATE TABLE dse_indices (
                id SERIAL PRIMARY KEY,
                index_description VARCHAR NOT NULL,
                closing_price FLOAT NOT NULL,
                change NUMERIC(15, 8) NOT NULL,
                code VARCHAR(255) NOT NULL
            );
        """
        cursor.execute(create_table_query)
        connection.commit()

# Check and create the table if absent
check_and_create_table(cursor)

# Insert data into the database
try:
    for item in indices_data:
        if isinstance(item, dict):
            index_description = item['IndexDescription']
            closing_price = float(item['ClosingPrice'].replace(",", "").strip())
            change = item['Change']
            code = item['Code']
            
            cursor.execute("""
                INSERT INTO dse_indices (index_description, closing_price, change, code)
                VALUES (%s, %s, %s, %s);
            """, (index_description, closing_price, change, code))
        else:
            print("Error: Could not insert item into the database:", item)

    connection.commit()
            
except Exception as e:
    print(f"Error: Could not insert data into the database: {e}")
    connection.rollback()
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
