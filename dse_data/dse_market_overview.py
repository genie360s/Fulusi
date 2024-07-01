import requests
import psycopg

from psycopg.rows import dict_row
from dotenv import load_dotenv
import os

load_dotenv()

market_overview_api_url = os.getenv("DSE_MARKET_OVERVIEW_URL")

# API request to get the gainers and losers
response_market_overview = requests.get(market_overview_api_url)

# Check if the request was successful
if response_market_overview.status_code == 200:
    market_overview_data = response_market_overview.json()
    del market_overview_data['success']

else:
    print("Error: Could not retrieve data from the API")
    print(response_market_overview.text)
    exit()

# Connect to the PostgreSQL database
try:
    connection = psycopg.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        # Fetch rows as dictionaries
        row_factory=dict_row  
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
            AND table_name = 'dse_market_overview'
        );
    """
    cursor.execute(table_check_query)
    table_exists = cursor.fetchone()['exists']
    if not table_exists:
        create_table_query = """
            CREATE TABLE dse_market_overview (
                id SERIAL PRIMARY KEY,
                volume FLOAT NOT NULL,
                market_cap_aggregate FLOAT NOT NULL,
                turn_over FLOAT NOT NULL,
                deals INTEGER NOT NULL,
                of_date DATE NOT NULL
            );
        """
        cursor.execute(create_table_query)
        connection.commit()

# Check and create the table if absent
check_and_create_table(cursor)

# Insert the data into the database
try:
    insert_query = """
        INSERT INTO dse_market_overview (volume, market_cap_aggregate, turn_over, deals, of_date)
        VALUES (%s, %s, %s, %s, %s);
    """
    
    # Format data for insertion
    formatted_data = (
        float(market_overview_data['volume'].replace(',', '')),
        float(market_overview_data['m_cap_aggregate'].replace(',', '')),
        float(market_overview_data['turn_over'].replace(',', '')),
        int(market_overview_data['deals']),
        market_overview_data['of_date'].split('T')[0]  # Assuming the date is already in ISO format
    )
    
    # Execute the insertion query
    cursor.execute(insert_query, formatted_data)
    connection.commit()
    print("Data inserted successfully!")
except Exception as e:
    connection.rollback()
    print("Error inserting data:")
    print(e)
finally:
    cursor.close()
    connection.close()
