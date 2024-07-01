"""
api_integration.py

## Purpose
The `api_integration.py` file is a critical part of our algorithmic trading project. It handles the integration with external APIs to fetch financial data from Yahoo Finance and Coinbase. This data is essential for developing and testing trading strategies. By automating the data retrieval process, we ensure that we always have up-to-date information for analysis and backtesting.

## Importance
Integrating with financial APIs is vital for:
1. **Access to Real-Time Data**: Fetching the latest stock and cryptocurrency data allows our algorithms to operate on current market conditions.
2. **Historical Data Analysis**: Retrieving historical data helps in backtesting and understanding past market trends.
3. **Strategy Development**: Having consistent access to financial data is crucial for developing and refining trading strategies.
4. **Automation**: Automating data retrieval saves time and reduces the potential for manual errors, ensuring accuracy and reliability in our data sources.

## Functionality
1. **Load Environment Variables**:
   - The script uses the `dotenv` package to load API keys and secrets from a `.env` file. This keeps sensitive information secure and separate from the source code.

2. **Fetch Data from Yahoo Finance**:
   - The function `get_yahoo_finance_data(ticker)` takes a stock ticker symbol as input and retrieves the corresponding stock data from Yahoo Finance.
   - It constructs the API request URL, adds the necessary headers (including the API key), and processes the response.

3. **Fetch Data from Coinbase**:
   - The function `get_coinbase_data(currency_pair)` takes a cryptocurrency pair (e.g., "BTC-USD") as input and retrieves the corresponding data from Coinbase.
   - It constructs the API request URL, adds the necessary headers (including the API key and secret), and processes the response.

4. **Helper Function for API Requests**:
   - The helper function `fetch_api_data(url, headers)` is used by both `get_yahoo_finance_data` and `get_coinbase_data` to handle the actual API requests.
   - This function manages the HTTP request, checks for successful responses, and handles any errors that may occur during the request.

5. **Save Data to CSV**:
   - The function `save_data_to_csv(data, filename)` takes the data fetched from the APIs and saves it into a CSV file using the `pandas` library.
   - It ensures that data is correctly structured before saving and handles cases where there is no data to save.

6. **Main Execution Block**:
   - The script can be executed directly, where it will fetch data for a specific stock ticker and cryptocurrency pair, then save the fetched data to CSV files.
   - This block provides example usage of the functions defined in the module, demonstrating how to fetch and save data.

## Example Usage
```python
if __name__ == "__main__":
    # Example usage
    
    # Fetch and save Yahoo Finance data
    ticker = "AAPL"
    yahoo_data = get_yahoo_finance_data(ticker)
    if yahoo_data:
        save_data_to_csv(yahoo_data, "yahoo_finance_data.csv")
    
    # Fetch and save Coinbase data
    currency_pair = "BTC-USD"
    coinbase_data = get_coinbase_data(currency_pair)
    if coinbase_data:
        save_data_to_csv(coinbase_data, "coinbase_data.csv")
"""



import os
from dotenv import load_dotenv
import requests
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Yahoo Finance API details
YAHOO_FINANCE_API_KEY = os.getenv("YAHOO_FINANCE_API_KEY")

# Coinbase API details
COINBASE_API_KEY = os.getenv("COINBASE_API_KEY")
COINBASE_API_SECRET = os.getenv("COINBASE_API_SECRET")

def fetch_api_data(url, headers):
    """
    Helper function to fetch data from an API endpoint.
    """
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None

def get_yahoo_finance_data(ticker):
    """
    Fetches stock data from Yahoo Finance for the given ticker symbol.
    """
    base_url = "https://yfapi.net/v8/finance/chart/"
    url = f"{base_url}{ticker}"
    headers = {"x-api-key": YAHOO_FINANCE_API_KEY}
    return fetch_api_data(url, headers)

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

def save_data_to_csv(data, filename):
    """
    Saves data to a CSV file.
    """
    if data:
        df = pd.DataFrame([data])  # Wrap data in a list to ensure correct DataFrame structure
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print(f"No data to save for {filename}")

if __name__ == "__main__":
    # Example usage

    # Fetch and save Yahoo Finance data
    ticker = "AAPL"
    yahoo_data = get_yahoo_finance_data(ticker)
    save_data_to_csv(yahoo_data, "yahoo_finance_data.csv")

    # Fetch and save Coinbase data
    currency_pair = "BTC-USD"
    coinbase_data = get_coinbase_data(currency_pair)
    save_data_to_csv(coinbase_data, "coinbase_data.csv")
