import requests
import psycopg
from dotenv import load_dotenv
import os
load_dotenv()

api_url = os.getenv("DSE_API_URL")

#api request to get the data

response = requests.get(api_url)

#check if the request was successful
if response.status_code == 200:
    data = response.json()
    stock_data = data['data']
    print(stock_data)
else:
    print("Error: Could not retrieve data from the API")
    print(response.text)
    exit()

# connect to the PostgreSQL database
try:
    connection = psycopg.connect(
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME")
    )
    cursor = connection.cursor()
except Exception as e:
    print("Error: Could not connect to the database")
    print(e)
    exit()

# check if the table exists if not create it
def check_and_create_table(cursor):
    table_check_query = """
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public'
            AND  table_name = 'dse_stock_prices'
        );
    """
    cursor.execute(table_check_query)
    table_exists = cursor.fetchone()[0]

    if not table_exists:
        create_table_query = """
            CREATE TABLE dse_stock_prices (
                id INTEGER PRIMARY KEY,
                company VARCHAR NOT NULL,
                price FLOAT NOT NULL,
                change FLOAT NOT NULL
            );
        """
        cursor.execute(create_table_query)
        connection.commit()

# Check and create the table if absent
check_and_create_table(cursor)

# Insert data into the database
try:
    for item in stock_data:  
        if isinstance(item, dict):
            item_id = int(item['id'])
            company = item['company']
            price = float(item['price'])
            change = float(item['change'])


            cursor.execute("""
                INSERT INTO dse_stock_prices (id, company, price, change)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
            """, (item_id, company, price, change))
        else:
            print("Error: Invalid item format:", item)
            

    # Commit the transaction
    connection.commit()
except Exception as e:
    print(f"Error inserting data into the database: {e}")
    connection.rollback()
finally:
    # Close the database connection
    cursor.close()
    connection.close()