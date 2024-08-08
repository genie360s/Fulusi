import requests
from requests.exceptions import Timeout
import os
from dotenv import load_dotenv
import pandas as pd

def collect_bank_forex_rates():
    load_dotenv() 
    base_api_url = os.getenv("BASE_API_URL")
    
    bank_names = [
        "azania_bank", "baroda_bank", "bank_of_india", 
        "bank_of_tanzania", "tanzania_commercial_bank", "dcb_bank", 
        "habib_africa_bank", "mkombozi_bank", "national_microfinance_bank", "amana_bank"
    ]
    
    # Initialize an empty DataFrame with a consistent structure
    bank_forex_df = pd.DataFrame(columns=["bank_name"])  # Start with a column for the bank name
    
    for bank_name in bank_names:
        bank_api_url = f"{base_api_url}/{bank_name}/latest_date"
        try:
            response = requests.get(bank_api_url)
            if response.status_code == 200:
                bank_forex_data = response.json()
                
                # Temporary dictionary to hold the data for the current bank
                temp_data = {"bank_name": bank_name}
                
                # Iterate over the data returned from the API
                for currency_data in bank_forex_data:
                    currency = currency_data.get("currency", "").upper()
                    buying_price = currency_data.get("buying_price", None)
                    selling_price = currency_data.get("selling_price", None)
                    
                    # Define the column names
                    buying_column = f"buying_price_in_{currency}"
                    selling_column = f"selling_price_in_{currency}"
                    
                    # Add data to the temp dictionary
                    temp_data[buying_column] = buying_price
                    temp_data[selling_column] = selling_price
                
                # Convert the temp_data dictionary to a DataFrame
                temp_df = pd.DataFrame(temp_data, index=[0])  # Single-row DataFrame
                
                # Append the temp_df to the main DataFrame
                bank_forex_df = pd.concat([bank_forex_df, temp_df], ignore_index=True)
                
            else:
                print(f"Failed to fetch data for {bank_name}. Status code: {response.status_code}")
                
        except Timeout:
            print(f"API request timed out for {bank_name}.")
        except Exception as e:
            print(f"Failed to fetch data from {bank_name}: {str(e)}")
    
    # Set the index to 'bank_name' to ensure proper row alignment
    bank_forex_df.set_index("bank_name", inplace=True)
    
    return bank_forex_df

