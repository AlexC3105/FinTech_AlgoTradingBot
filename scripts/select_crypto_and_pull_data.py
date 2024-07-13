"""
select_crypto_and_pull_data.py

## Purpose
The `select_crypto_and_pull_data.py` file is designed to provide an interactive way for users to select a cryptocurrency and fetch its historical data. This script simplifies the process of data retrieval by guiding the user through a selection menu and then using the Alpha Vantage API to download the historical price data for the chosen cryptocurrency. The fetched data is then saved to a CSV file for further analysis.

## Importance
This script is essential for several reasons:
1. **User-Friendly Interface**: It provides a simple and interactive way for users to select a cryptocurrency and fetch its data without needing to manually enter API requests.
2. **Automation**: Automates the process of data retrieval, ensuring that data is fetched and stored consistently.
3. **Integration**: Acts as a bridge between user input and the data retrieval functions defined in other scripts (e.g., `api_integration.py`), making it easy to fetch data for various cryptocurrencies.
4. **Scalability**: Can be easily extended to support additional cryptocurrencies or data sources as needed.

## Functionality
1. **Cryptocurrency Selection**:
   - The script presents a menu of available cryptocurrencies for the user to choose from.
   - The user selects a cryptocurrency by entering the corresponding number.

2. **Data Fetching**:
   - The script calls the `fetch_data` function from `api_integration.py` to retrieve historical data for the selected cryptocurrency.
   - The fetched data is saved to a CSV file in the `data/historical_data/` folder.

3. **Error Handling**:
   - The script includes basic error handling to manage invalid user inputs and failed data fetch attempts.

## Example Usage
```python
import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

def fetch_data(symbol, output_file):
    '''
    Fetch historical data for a given cryptocurrency symbol from Alpha Vantage API and save to CSV.
    
    Parameters:
    symbol (str): Cryptocurrency symbol (e.g., 'BTC-USD').
    output_file (str): Path to the output CSV file.
    
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market=USD&apikey={ALPHA_VANTAGE_API_KEY}&datatype=csv"
    response = requests.get(url)
    '''
    if response.status_code == 200:
        with open(output_file, 'wb') as file:
            file.write(response.content)
        print(f"Data for {symbol} saved to {output_file}")
    else:
        print(f"Failed to fetch data for {symbol}. Status code: {response.status_code}")

if __name__ == "__main__":
    crypto_map = {
        "1": ("BTC-USD", "data/historical_data/btc_usd.csv"),
        "2": ("ETH-USD", "data/historical_data/eth_usd.csv"),
        "3": ("SOL-USD", "data/historical_data/sol_usd.csv")
    }

    print("Select a cryptocurrency to fetch data for:")
    print("1: Bitcoin (BTC-USD)")
    print("2: Ethereum (ETH-USD)")
    print("3: Solana (SOL-USD)")
    choice = input("Enter the number corresponding to the cryptocurrency: ")

    if choice in crypto_map:
        symbol, output_file = crypto_map[choice]
        print(f"Fetching data for {symbol}...")
        fetch_data(symbol, output_file)
    else:
        print("Invalid choice. Please run the script again and select a valid option.")
"""



import os
import requests
from dotenv import load_dotenv
import argparse

# Load environment variables from .env file
load_dotenv()

ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

def fetch_data(symbol, output_file):
    """
    Fetch historical data for a given cryptocurrency symbol from Alpha Vantage API and save to CSV.
    
    Parameters:
    symbol (str): Cryptocurrency symbol (e.g., 'BTC-USD').
    output_file (str): Path to the output CSV file.
    """
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market=USD&apikey={ALPHA_VANTAGE_API_KEY}&datatype=csv"
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(output_file, 'wb') as file:
            file.write(response.content)
        print(f"Data for {symbol} saved to {output_file}")
    else:
        print(f"Failed to fetch data for {symbol}. Status code: {response.status_code}")

def handle_all():
    """
    Fetch data for all cryptocurrencies and save to respective CSV files.
    """
    crypto_map = {
        "BTC": ("BTC-USD", "data/historical_data/btc_usd.csv"),
        "ETH": ("ETH-USD", "data/historical_data/eth_usd.csv"),
        "SOL": ("SOL-USD", "data/historical_data/sol_usd.csv")
    }
    
    for symbol, (api_symbol, output_file) in crypto_map.items():
        print(f"Fetching data for {api_symbol}...")
        fetch_data(api_symbol, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch cryptocurrency data.')
    parser.add_argument('--crypto', type=str, required=True, choices=['BTC', 'ETH', 'SOL', 'ALL'], help='The cryptocurrency symbol (e.g., BTC, ETH, SOL, ALL).')
    
    args = parser.parse_args()
    
    if args.crypto == 'ALL':
        handle_all()
    else:
        crypto_map = {
            "BTC": ("BTC-USD", "data/historical_data/btc_usd.csv"),
            "ETH": ("ETH-USD", "data/historical_data/eth_usd.csv"),
            "SOL": ("SOL-USD", "data/historical_data/sol_usd.csv")
        }

        symbol, output_file = crypto_map[args.crypto]
        print(f"Fetching data for {symbol}...")
        fetch_data(symbol, output_file)
