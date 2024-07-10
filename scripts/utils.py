"""
utils.py

## Purpose
The `utils.py` file is a utility script that provides various helper functions for data processing and analysis. These functions are designed to streamline repetitive tasks and make the codebase more modular and maintainable. By centralizing common operations into this script, we can ensure consistency and reduce code duplication across different parts of the project.

## Importance
Having a dedicated utility script is essential for several reasons:
1. **Modularity**: It keeps the codebase organized by separating utility functions from the core logic, making it easier to understand and maintain.
2. **Reusability**: The functions defined in this script can be reused across multiple notebooks and scripts, promoting code reuse and reducing duplication.
3. **Consistency**: By using the same utility functions throughout the project, we ensure that data processing and analysis are performed consistently.
4. **Efficiency**: It simplifies the code in other parts of the project by offloading common tasks to this script, making the overall codebase cleaner and more efficient.

## Functionality
1. **Load Data**:
   - The `load_data` function reads historical price data from a CSV file and returns it as a pandas DataFrame.

2. **Preprocess Data**:
   - The `preprocess_data` function cleans and preprocesses the data, handling missing values and sorting by date.

3. **Calculate Indicators**:
   - The `calculate_indicators` function adds technical indicators (e.g., SMA, EMA, RSI) to the data, which are used for analysis and model training.

4. **Calculate RSI**:
   - The `calculate_rsi` function calculates the Relative Strength Index (RSI) for a given time series, providing insights into market momentum.

## Example Usage
### Load Data
```python
import pandas as pd
from scripts.utils import load_data

# Load historical price data
data_path = 'data/historical_data/btc_usd.csv'
data = load_data(data_path)

# Display the first few rows of the data
data.head()

"""



import pandas as pd

def load_data(file_path):
    """
    Load historical price data from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file.
    
    Returns:
    pd.DataFrame: Loaded data.
    """
    return pd.read_csv(file_path, parse_dates=['Date'])

def preprocess_data(data):
    """
    Preprocess the historical price data.
    
    Parameters:
    data (pd.DataFrame): Historical price data.
    
    Returns:
    pd.DataFrame: Preprocessed data.
    """
    data = data.sort_values('Date')
    data.set_index('Date', inplace=True)
    data.fillna(method='ffill', inplace=True)
    return data

def calculate_indicators(data):
    """
    Calculate technical indicators for the data.
    
    Parameters:
    data (pd.DataFrame): Historical price data.
    
    Returns:
    pd.DataFrame: Data with technical indicators.
    """
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()
    data['EMA_50'] = data['Close'].ewm(span=50, adjust=False).mean()
    data['RSI'] = calculate_rsi(data['Close'])
    return data

def calculate_rsi(series, period=14):
    """
    Calculate the Relative Strength Index (RSI) for a series.
    
    Parameters:
    series (pd.Series): Time series data.
    period (int): Lookback period for RSI calculation.
    
    Returns:
    pd.Series: RSI values.
    """
    delta = series.diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

if __name__ == "__main__":
    data = load_data('data/historical_data/btc_usd.csv')
    data = preprocess_data(data)
    data = calculate_indicators(data)
    print(data.head())
