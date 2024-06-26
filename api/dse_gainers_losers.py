import requests
import psycopg

from dotenv import load_dotenv
import os

load_dotenv()

dse_gainers_losers_api_url = os.getenv("DSE_GAINERS_LOSERS_URL")

#api request to get the data

response = requests.get(dse_gainers_losers_api_url)

#check if the request was successful
if response.status_code == 200:
    data = response.json()
    gainer_losers_data = data['gainers_and_losers']
    print(gainer_losers_data)
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
            AND  table_name = 'dse_gainers_losers'
        );
    """
    cursor.execute(table_check_query)
    table_exists = cursor.fetchone()[0]

    if not table_exists:
        create_table_query = """
            CREATE TABLE dse_gainers_losers (
                id SERIAL PRIMARY KEY,
                company VARCHAR NOT NULL,
                change NUMERIC NOT NULL,
                price FLOAT NOT NULL,
                volume INTEGER NOT NULL
            );
        """
        cursor.execute(create_table_query)
        connection.commit()

check_and_create_table(cursor)

# insert the data into the table
try:
    for item in gainer_losers_data:
        if isinstance (item, dict):
            company = item['company']
            change = item['change']
            price = float(item['price'].replace(",", "").strip())
            volume = int(item['volume'].replace(",", "").strip())

            cursor.execute("""
                INSERT INTO dse_gainers_losers (company, change, price, volume)
                VALUES (%s, %s, %s, %s)
            """, (company, change, price, volume))
        else:
            print("Error: Invalid data format")
            

    # commit the transaction
    connection.commit()

except Exception as e:
    print(f"Error: Could not insert data into the database: {e}")
    connection.rollback()
finally:
    # close the connection
    cursor.close()
    connection.close()