"""
interface.py

## Purpose
The `interface.py` file is designed to provide a user-friendly interface for interacting with the Algo Trading project. It simplifies the process of selecting a cryptocurrency, fetching historical data, and retrieving Alpaca account information. This script serves as a bridge between the user and the core functionalities of the project, making it easier to perform common tasks without directly interacting with the codebase.

## Importance
Having an interface script is essential for several reasons:
1. **User Convenience**: It provides a straightforward way for users to interact with the project, even if they are not proficient in coding.
2. **Consistency**: It ensures that data fetching and other tasks are performed in a consistent manner, reducing the risk of errors.
3. **Integration**: It integrates different parts of the project, such as data fetching and account information retrieval, into a single, easy-to-use interface.
4. **Automation**: It automates repetitive tasks, saving time and effort for users.

## Functionality
1. **Fetch Cryptocurrency Data**:
   - The script allows users to select a cryptocurrency from a list and fetch historical data for the selected cryptocurrency using the `fetch_data` function from `api_integration.py`.
   - The data is saved to a CSV file in the `data/historical_data/` folder.

2. **Get Alpaca Account Information**:
   - The script uses environment variables to retrieve Alpaca API keys and connects to the Alpaca API to fetch account information.
   - This functionality is useful for users who want to verify their Alpaca account status or check their account balance.

3. **Integration with Other Scripts**:
   - The `interface.py` script integrates seamlessly with other scripts in the project, such as `api_integration.py`, to provide a unified interface for the user.

## Example Usage
```python
import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from scripts.api_integration import fetch_data

def fetch_crypto_data():
    print("Select a cryptocurrency to fetch data for:")
    print("1: Bitcoin (BTC-USD)")
    print("2: Ethereum (ETH-USD)")
    print("3: Solana (SOL-USD)")
    choice = input("Enter the number corresponding to the cryptocurrency: ")

    crypto_map = {
        "1": ("BTC-USD", "data/historical_data/btc_usd.csv"),
        "2": ("ETH-USD", "data/historical_data/eth_usd.csv"),
        "3": ("SOL-USD", "data/historical_data/sol_usd.csv")
    }

    if choice in crypto_map:
        symbol, output_file = crypto_map[choice]
        print(f"Fetching data for {symbol}...")
        fetch_data(symbol, output_file)
        print(f"Data saved to {output_file}")
    else:
        print("Invalid choice. Please run the script again and select a valid option.")

def get_alpaca_account_info():
    load_dotenv()
    ALPACA_API_KEY_ID = os.getenv('ALPACA_API_KEY_ID')
    ALPACA_SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')
    ALPACA_BASE_URL = os.getenv('ALPACA_BASE_URL')

    api = tradeapi.REST(ALPACA_API_KEY_ID, ALPACA_SECRET_KEY, ALPACA_BASE_URL, api_version='v2')
    account = api.get_account()
    return account

if __name__ == "__main__":
    fetch_crypto_data()
    account_info = get_alpaca_account_info()
    print("Alpaca Account Info:", account_info)

"""



import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from scripts.api_integration import fetch_data

def fetch_crypto_data():
    print("Select a cryptocurrency to fetch data for:")
    print("1: Bitcoin (BTC-USD)")
    print("2: Ethereum (ETH-USD)")
    print("3: Solana (SOL-USD)")
    choice = input("Enter the number corresponding to the cryptocurrency: ")

    crypto_map = {
        "1": ("BTC-USD", "data/historical_data/btc_usd.csv"),
        "2": ("ETH-USD", "data/historical_data/eth_usd.csv"),
        "3": ("SOL-USD", "data/historical_data/sol_usd.csv")
    }

    if choice in crypto_map:
        symbol, output_file = crypto_map[choice]
        print(f"Fetching data for {symbol}...")
        fetch_data(symbol, output_file)
        print(f"Data saved to {output_file}")
    else:
        print("Invalid choice. Please run the script again and select a valid option.")

def get_alpaca_account_info():
    load_dotenv()
    ALPACA_API_KEY_ID = os.getenv('ALPACA_API_KEY_ID')
    ALPACA_SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')
    ALPACA_BASE_URL = os.getenv('ALPACA_BASE_URL')

    api = tradeapi.REST(ALPACA_API_KEY_ID, ALPACA_SECRET_KEY, ALPACA_BASE_URL, api_version='v2')
    account = api.get_account()
    return account

if __name__ == "__main__":
    fetch_crypto_data()
    account_info = get_alpaca_account_info()
    print("Alpaca Account Info:", account_info)
