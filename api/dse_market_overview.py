import requests
import psycopg

from psycopg.rows import dict_row
from dotenv import load_dotenv
import os

load_dotenv()

gainers_losers_api_url = os.getenv("DSE_MARKET_OVERVIEW_URL")

# API request to get the gainers and losers
response_gainers_losers = requests.get(gainers_losers_api_url)

# Check if the request was successful
if response_gainers_losers.status_code == 200:
    gainers_losers_data = response_gainers_losers.json()
    del gainers_losers_data['success']

else:
    print("Error: Could not retrieve data from the API")
    print(response_gainers_losers.text)
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
            AND table_name = 'dse_gainers_losers'
        );
    """
    cursor.execute(table_check_query)
    table_exists = cursor.fetchone()['exists']
    if not table_exists:
        create_table_query = """
            CREATE TABLE dse_gainers_losers (
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
        INSERT INTO dse_gainers_losers (volume, market_cap_aggregate, turn_over, deals, of_date)
        VALUES (%s, %s, %s, %s, %s);
    """
    
    # Format data for insertion
    formatted_data = (
        float(gainers_losers_data['volume'].replace(',', '')),
        float(gainers_losers_data['m_cap_aggregate'].replace(',', '')),
        float(gainers_losers_data['turn_over'].replace(',', '')),
        int(gainers_losers_data['deals']),
        gainers_losers_data['of_date'].split('T')[0]  # Assuming the date is already in ISO format
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
