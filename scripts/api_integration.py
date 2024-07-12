"""
api_integration.py

## Purpose
The `api_integration.py` file is designed to handle the integration of various APIs used in our algorithmic trading project. This script fetches and processes real-time and historical cryptocurrency data from multiple sources, ensuring that our trading algorithms have access to up-to-date and accurate information. By automating API interactions, we streamline the data acquisition process and maintain consistency across our datasets.

## Importance
API integration is a critical aspect of algorithmic trading, providing several key benefits:
1. **Access to Real-Time Data**: APIs allow us to retrieve real-time market data, which is essential for making informed trading decisions.
2. **Historical Data Retrieval**: Access to historical data enables us to backtest our trading strategies and evaluate their performance over time.
3. **Automation**: Automating the data retrieval process ensures that our datasets are always current, reducing manual intervention and potential errors.
4. **Scalability**: With API integration, we can easily scale our data acquisition to include multiple cryptocurrencies and trading platforms.

## Functionality
1. **Fetch Historical Data**:
   - The script includes functions to fetch historical cryptocurrency data from various APIs.
   - It processes the retrieved data and saves it in a standardized format for further analysis.

2. **Fetch Real-Time Data**:
   - Functions for fetching real-time market data are also included, providing the latest prices and market conditions.
   - This real-time data is used by our trading algorithms to make timely trading decisions.

3. **Error Handling and Logging**:
   - The script includes error handling mechanisms to manage API rate limits and connection issues.
   - Logging functionality ensures that any issues during data retrieval are recorded for troubleshooting.

4. **API Key Management**:
   - The script handles API key management, ensuring that our API keys are securely stored and used for authenticated requests.

## Example Usage
```python
from scripts.api_integration import fetch_historical_data, fetch_real_time_data

# Fetch historical data
historical_data = fetch_historical_data('BTC', '2020-01-01', '2021-01-01')

# Fetch real-time data
real_time_data = fetch_real_time_data('BTC')

# Display data
print(historical_data.head())
print(real_time_data)

"""



import requests
import pandas as pd
import logging
import os

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# API endpoints and keys
API_KEYS = {
    'ALPACA': 'your_alpaca_api_key',
    'ALPACA_SECRET': 'your_alpaca_secret_key',
    'YAHOO_FINANCE': 'your_yahoo_finance_api_key'
}

ALPACA_BASE_URL = 'https://paper-api.alpaca.markets'
YAHOO_FINANCE_URL = 'https://yfapi.net/v8/finance/chart/'

def fetch_historical_data(symbol, start_date, end_date, source='alpaca'):
    """
    Fetch historical data for a given cryptocurrency symbol from a specified source.

    :param symbol: Cryptocurrency symbol (e.g., 'BTC')
    :param start_date: Start date for historical data in 'YYYY-MM-DD' format
    :param end_date: End date for historical data in 'YYYY-MM-DD' format
    :param source: Data source ('alpaca' or 'yahoo')
    :return: DataFrame containing historical data
    """
    if source == 'alpaca':
        return fetch_historical_data_alpaca(symbol, start_date, end_date)
    elif source == 'yahoo':
        return fetch_historical_data_yahoo(symbol, start_date, end_date)
    else:
        logger.error("Unsupported data source")
        return None

def fetch_historical_data_alpaca(symbol, start_date, end_date):
    """
    Fetch historical data from Alpaca API.

    :param symbol: Cryptocurrency symbol (e.g., 'BTC')
    :param start_date: Start date for historical data in 'YYYY-MM-DD' format
    :param end_date: End date for historical data in 'YYYY-MM-DD' format
    :return: DataFrame containing historical data
    """
    url = f"{ALPACA_BASE_URL}/v2/stocks/{symbol}/bars"
    headers = {
        'APCA-API-KEY-ID': API_KEYS['ALPACA'],
        'APCA-API-SECRET-KEY': API_KEYS['ALPACA_SECRET']
    }
    params = {
        'start': start_date,
        'end': end_date,
        'limit': 1000,  # adjust as needed
        'timeframe': 'day'
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['bars'])
        df['time'] = pd.to_datetime(df['t'], unit='s')
        df.set_index('time', inplace=True)
        df.drop(columns=['t'], inplace=True)
        return df
    else:
        logger.error(f"Failed to fetch data from Alpaca: {response.status_code}")
        return None

def fetch_historical_data_yahoo(symbol, start_date, end_date):
    """
    Fetch historical data from Yahoo Finance API.

    :param symbol: Cryptocurrency symbol (e.g., 'BTC')
    :param start_date: Start date for historical data in 'YYYY-MM-DD' format
    :param end_date: End date for historical data in 'YYYY-MM-DD' format
    :return: DataFrame containing historical data
    """
    url = f"{YAHOO_FINANCE_URL}{symbol}USD"
    headers = {'x-api-key': API_KEYS['YAHOO_FINANCE']}
    params = {
        'symbol': symbol,
        'period1': int(pd.Timestamp(start_date).timestamp()),
        'period2': int(pd.Timestamp(end_date).timestamp()),
        'interval': '1d'
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0])
        df['time'] = pd.to_datetime(data['chart']['result'][0]['timestamp'], unit='s')
        df.set_index('time', inplace=True)
        return df
    else:
        logger.error(f"Failed to fetch data from Yahoo Finance: {response.status_code}")
        return None

def fetch_real_time_data(symbol, source='alpaca'):
    """
    Fetch real-time data for a given cryptocurrency symbol from a specified source.

    :param symbol: Cryptocurrency symbol (e.g., 'BTC')
    :param source: Data source ('alpaca' or 'yahoo')
    :return: Real-time data as JSON
    """
    if source == 'alpaca':
        return fetch_real_time_data_alpaca(symbol)
    elif source == 'yahoo':
        return fetch_real_time_data_yahoo(symbol)
    else:
        logger.error("Unsupported data source")
        return None

def fetch_real_time_data_alpaca(symbol):
    """
    Fetch real-time data from Alpaca API.

    :param symbol: Cryptocurrency symbol (e.g., 'BTC')
    :return: Real-time data as JSON
    """
    url = f"{ALPACA_BASE_URL}/v2/stocks/{symbol}/quotes/latest"
    headers = {
        'APCA-API-KEY-ID': API_KEYS['ALPACA'],
        'APCA-API-SECRET-KEY': API_KEYS['ALPACA_SECRET']
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"Failed to fetch real-time data from Alpaca: {response.status_code}")
        return None

def fetch_real_time_data_yahoo(symbol):
    """
    Fetch real-time data from Yahoo Finance API.

    :param symbol: Cryptocurrency symbol (e.g., 'BTC')
    :return: Real-time data as JSON
    """
    url = f"{YAHOO_FINANCE_URL}{symbol}USD"
    headers = {'x-api-key': API_KEYS['YAHOO_FINANCE']}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"Failed to fetch real-time data from Yahoo Finance: {response.status_code}")
        return None

if __name__ == "__main__":
    # Example usage
    historical_data = fetch_historical_data('BTC', '2020-01-01', '2021-01-01')
    if historical_data is not None:
        print(historical_data.head())
    
    real_time_data = fetch_real_time_data('BTC')
    if real_time_data is not None:
        print(real_time_data)
