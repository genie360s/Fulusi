import requests
from requests.exceptions import Timeout
import os
from dotenv import load_dotenv
from flask import  jsonify
import json
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


def check_for_best_selling_and_buying_prices():
    bank_forex_df = collect_bank_forex_rates()
    bank_forex_df_filled = bank_forex_df.fillna(0)
    
    # Convert all columns except the first to float
    bank_forex_df_filled.iloc[:, 1:] = bank_forex_df_filled.iloc[:, 1:].astype(float)

    # Identify columns related to buying and selling prices
    buying_columns = [col for col in bank_forex_df_filled.columns if col.startswith("buying_price")]
    selling_columns = [col for col in bank_forex_df_filled.columns if col.startswith("selling_price")]

    # Find the bank with the highest buying rate for each currency
    banks_with_best_buying_price = bank_forex_df_filled[buying_columns].idxmax()
    highest_buying_values = bank_forex_df_filled[buying_columns].max()

    # Find the bank with the lowest selling rate for each currency, excluding zeros
    lowest_selling_values = bank_forex_df_filled[selling_columns].apply(lambda x: x[x > 0].min())
    banks_with_best_selling_price = bank_forex_df_filled[selling_columns].apply(lambda x: x[x > 0].idxmin())

    # Compile the results into a summary DataFrame
    summary = pd.DataFrame({
        "currency": banks_with_best_buying_price.index.str.replace("buying_price_in_", "").str.replace("selling_price_in_", ""),
        "best_buying_price": highest_buying_values.values,
        "bank_with_best_buying_price": banks_with_best_buying_price.values,
        "best_selling_price": lowest_selling_values.values,
        "bank_with_best_selling_price": banks_with_best_selling_price.values
    })

    # Convert the DataFrame to a list of dictionaries
    best_bank_rates = summary.to_dict(orient="records")


    # Display the JSON output
    print("\n best bank rates :")
    print(jsonify(best_bank_rates))
    
    return jsonify(best_bank_rates)

def get_forex_rates_in_summary():
    bank_forex_df = collect_bank_forex_rates()
    bank_forex_df_filled = bank_forex_df.fillna(0)
    
    # Convert all columns except the first to float
    bank_forex_df_filled.iloc[:, 1:] = bank_forex_df_filled.iloc[:, 1:].astype(float)

    # Initialize an empty dictionary to store the final results
    forex_rates = {}

    # Iterate over each currency in the DataFrame
    currencies = set([col.split('_in_')[1] for col in bank_forex_df_filled.columns if 'price_in_' in col])
    for currency in currencies:
        currency_data = {}
        selling_prices = {}
        buying_prices = {}

        # Collect selling prices that are non-zero
        selling_column = f"selling_price_in_{currency}"
        for bank_name, selling_price in bank_forex_df_filled[selling_column].items():
            if selling_price > 0:
                selling_prices[bank_name] = selling_price
        
        # Collect buying prices that are non-zero
        buying_column = f"buying_price_in_{currency}"
        for bank_name, buying_price in bank_forex_df_filled[buying_column].items():
            if buying_price > 0:
                buying_prices[bank_name] = buying_price

        if selling_prices or buying_prices:
            currency_data['selling_prices'] = selling_prices
            currency_data['buying_prices'] = buying_prices
            forex_rates[currency] = currency_data

    

    # Display the JSON output
    print("\nForex Rates:")
    print(jsonify(forex_rates))

    return jsonify(forex_rates)
