import os
import requests
import pandas as pd
from dotenv import load_dotenv

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
