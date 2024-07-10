"""
api_integration.py

## Purpose
The `api_integration.py` file is a critical part of our algorithmic trading project. It handles the integration with external APIs to fetch financial data from Coinbase, Alpha Vantage, and CryptoCompare. This data is essential for developing and testing trading strategies. By automating the data retrieval process, we ensure that we always have up-to-date information for analysis and backtesting.

## Importance
Integrating with financial APIs is vital for:
1. **Access to Real-Time Data**: Fetching the latest stock and cryptocurrency data allows our algorithms to operate on current market conditions.
2. **Historical Data Analysis**: Retrieving historical data helps in backtesting and understanding past market trends.
3. **Strategy Development**: Having consistent access to financial data is crucial for developing and refining trading strategies.
4. **Automation**: Automating data retrieval saves time and reduces the potential for manual errors, ensuring accuracy and reliability in our data sources.

## Functionality
1. **Load Environment Variables**:
   - The script uses the `dotenv` package to load API keys and secrets from a `.env` file. This keeps sensitive information secure and separate from the source code.

2. **Fetch Data from Coinbase**:
   - The function `get_coinbase_data(currency_pair)` takes a cryptocurrency pair (e.g., "BTC-USD") as input and retrieves the corresponding data from Coinbase.
   - It constructs the API request URL, adds the necessary headers (including the API key and secret), and processes the response.

3. **Fetch Data from Alpha Vantage**:
   - The function `get_alpha_vantage_data(symbol)` takes a cryptocurrency symbol (e.g., "BTC") as input and retrieves the corresponding historical data from Alpha Vantage.
   - It constructs the API request URL, adds the necessary headers, and processes the response.

4. **Fetch Data from CryptoCompare**:
   - The function `get_cryptocompare_data(symbol, start_date, end_date)` takes a cryptocurrency symbol (e.g., "BTC") and date range as input and retrieves the corresponding historical data from CryptoCompare.
   - It constructs the API request URL, adds the necessary headers, and processes the response.

5. **Helper Function for API Requests**:
   - The helper function `fetch_api_data(url, headers)` is used by `get_coinbase_data`, `get_alpha_vantage_data`, and `get_cryptocompare_data` to handle the actual API requests.
   - This function manages the HTTP request, checks for successful responses, and handles any errors that may occur during the request.

6. **Save Data to CSV**:
   - The function `save_data_to_csv(data, filename)` takes the data fetched from the APIs and saves it into a CSV file using the `pandas` library.
   - It ensures that data is correctly structured before saving and handles cases where there is no data to save.

7. **Main Execution Block**:
   - The script can be executed directly, where it will fetch data for a specific cryptocurrency pair and symbol, then save the fetched data to CSV files.
   - This block provides example usage of the functions defined in the module, demonstrating how to fetch and save data.

## Example Usage
```python
if __name__ == "__main__":
    # Example usage
    
    # Fetch and save Coinbase data
    currency_pair = "BTC-USD"
    coinbase_data = get_coinbase_data(currency_pair)
    if coinbase_data:
        save_data_to_csv(coinbase_data, "coinbase_data.csv")
    
    # Fetch and save Alpha Vantage data
    symbol = "BTC"
    alpha_vantage_data = get_alpha_vantage_data(symbol)
    if alpha_vantage_data:
        save_data_to_csv(alpha_vantage_data, "alpha_vantage_data.csv")
    
    # Fetch and save CryptoCompare data
    symbol = "BTC"
    start_date = "2020-01-01"
    end_date = "2023-01-01"
    cryptocompare_data = get_cryptocompare_data(symbol, start_date, end_date)
    if cryptocompare_data:
        save_data_to_csv(cryptocompare_data, "cryptocompare_data.csv")
```
"""

import os
from dotenv import load_dotenv
import requests
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Coinbase API details
COINBASE_API_KEY = os.getenv("COINBASE_API_KEY")
COINBASE_API_SECRET = os.getenv("COINBASE_API_SECRET")

# Alpha Vantage API details
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

# CryptoCompare API details
CRYPTOCOMPARE_API_KEY = os.getenv("CRYPTOCOMPARE_API_KEY")

def fetch_api_data(url, headers=None, params=None):
    """
    Helper function to fetch data from an API endpoint.
    """
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None

def get_coinbase_data(currency_pair):
    """
    Fetches cryptocurrency data from Coinbase for the given currency pair.
    """
    base_url = "https://api.coinbase.com/v2/prices/"
    url = f"{base_url}{currency_pair}/spot"
    headers = {
        "CB-ACCESS-KEY": COINBASE_API_KEY,
        "CB-ACCESS-SIGN": COINBASE_API_SECRET
    }
    return fetch_api_data(url, headers)

def get_alpha_vantage_data(symbol):
    """
    Fetches cryptocurrency data from Alpha Vantage for the given symbol.
    """
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": symbol,
        "market": "USD",
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        if 'Time Series (Digital Currency Daily)' in data:
            time_series = data['Time Series (Digital Currency Daily)']
            df = pd.DataFrame.from_dict(time_series, orient='index')
            df = df.rename(columns={
                '1a. open (USD)': 'open',
                '2a. high (USD)': 'high',
                '3a. low (USD)': 'low',
                '4a. close (USD)': 'close',
                '5. volume': 'volume'
            })
            df.index = pd.to_datetime(df.index)
            df.reset_index(inplace=True)
            df = df.rename(columns={'index': 'time'})
            return df
        else:
            print(f"No 'Time Series (Digital Currency Daily)' data found for {symbol}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None

def get_cryptocompare_data(symbol, start_date, end_date):
    """
    Fetches cryptocurrency data from CryptoCompare for the given symbol and date range.
    """
    base_url = f"https://min-api.cryptocompare.com/data/v2/histoday"
    params = {
        "fsym": symbol,
        "tsym": "USD",
        "toTs": int(pd.Timestamp(end_date).timestamp()),
        "limit": 2000,  # CryptoCompare allows fetching up to 2000 days in one call
        "api_key": CRYPTOCOMPARE_API_KEY
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        if 'Data' in data and 'Data' in data['Data']:
            data = data['Data']['Data']
            df = pd.DataFrame(data)
            df['time'] = pd.to_datetime(df['time'], unit='s')
            df = df.rename(columns={'open': 'open', 'high': 'high', 'low': 'low', 'close': 'close', 'volumeto': 'volume'})
            df = df[['time', 'open', 'high', 'low', 'close', 'volume']]
            return df
        else:
            print(f"No data available for {symbol} from CryptoCompare")
            return None
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None

def save_data_to_csv(data, filename):
    """
    Saves data to a CSV file.
    """
    if data is not None and not data.empty:
        data.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print(f"No data to save for {filename}")

if __name__ == "__main__":
    cryptos = ["BTC", "ETH", "SOL"]
    start_date = "2018-01-01"
    end_date = "2023-01-01"

    for crypto in cryptos:
        # Fetch and save Coinbase data
        currency_pair = f"{crypto}-USD"
        coinbase_data = get_coinbase_data(currency_pair)
        save_data_to_csv(coinbase_data, f"data/historical_data/{crypto}_coinbase.csv")

        # Fetch and save Alpha Vantage data
        alpha_vantage_data = get_alpha_vantage_data(crypto)
        save_data_to_csv(alpha_vantage_data, f"data/historical_data/{crypto}_alpha_vantage.csv")

        # Fetch and save CryptoCompare data
        cryptocompare_data = get_cryptocompare_data(crypto, start_date, end_date)
        save_data_to_csv(cryptocompare_data, f"data/historical_data/{crypto}_cryptocompare.csv")

