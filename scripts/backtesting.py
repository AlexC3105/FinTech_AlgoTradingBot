"""
backtesting.py

## Purpose
The `backtesting.py` file is a crucial component of our algorithmic trading project. It automates the process of evaluating trading strategies by applying them to historical cryptocurrency data. This script allows us to assess the performance of our trading algorithms and understand their effectiveness in different market conditions. By automating the backtesting process, we ensure consistency, repeatability, and efficiency in our evaluations.

## Importance
Backtesting is an essential step in developing and validating trading strategies. It helps us to:
1. **Evaluate Strategy Performance**: By applying our trading strategies to historical data, we can analyze how well they would have performed in the past.
2. **Identify Strengths and Weaknesses**: Backtesting reveals the strengths and weaknesses of our strategies, allowing us to make informed decisions on potential adjustments and improvements.
3. **Risk Management**: Understanding the potential risks and returns of a strategy helps us manage and mitigate risks effectively.
4. **Optimize Parameters**: Through backtesting, we can experiment with different strategy parameters and identify the optimal settings for maximum performance.

## Functionality
1. **Run Backtest**:
   - The primary function in this script is `run_backtest`, which applies a given trading strategy to the historical data.
   - The function simulates trades based on the strategy's signals (buy, sell, hold) and tracks the performance of the portfolio over time.
   - It calculates key performance metrics such as portfolio value, cash balance, and position size.

2. **Strategy Definition**:
   - The script includes an example strategy function, `example_strategy`, which generates trading signals based on a simple moving average crossover.
   - Users can define their own strategies by modifying this function or adding new strategy functions.

3. **Automating Notebooks**:
   - This script complements the interactive Jupyter notebooks by automating the backtesting process.
   - While the notebook `05_backtesting.ipynb` allows for interactive exploration and visualization, `backtesting.py` provides a streamlined, repeatable approach to running backtests programmatically.
   - This automation ensures that our backtests are consistent and can be easily rerun with different parameters or datasets.

## Example Usage
```python
import pandas as pd
from scripts.backtesting import run_backtest, example_strategy

# Load preprocessed data
data_path = 'data/historical_data/btc_usd_preprocessed.csv'
data = pd.read_csv(data_path, parse_dates=['Date'], index_col='Date')

# Run backtest
results = run_backtest(data, example_strategy)

# Save backtest results
results.to_csv('results/backtest_results.csv')

# Display backtest results
results.head()

"""



import pandas as pd
import numpy as np

def run_backtest(data, strategy, initial_cash=10000):
    """
    Run a backtest for a given trading strategy.
    
    Parameters:
    data (pd.DataFrame): Historical price data.
    strategy (function): Trading strategy function.
    initial_cash (float): Initial amount of cash for backtesting.
    
    Returns:
    pd.DataFrame: DataFrame with backtesting results.
    """
    cash = initial_cash
    position = 0
    portfolio_value = initial_cash
    
    results = []
    
    for index, row in data.iterrows():
        signal = strategy(row)
        
        if signal == 'buy' and cash > 0:
            position = cash / row['Close']
            cash = 0
        elif signal == 'sell' and position > 0:
            cash = position * row['Close']
            position = 0
        
        portfolio_value = cash + (position * row['Close'])
        results.append({
            'Date': index,
            'Cash': cash,
            'Position': position,
            'Portfolio Value': portfolio_value
        })
    
    return pd.DataFrame(results)

def example_strategy(row):
    """
    Example strategy function.
    
    Parameters:
    row (pd.Series): A row of historical price data.
    
    Returns:
    str: 'buy', 'sell', or 'hold' signal.
    """
    short_window = 40
    long_window = 100
    
    if 'short_mavg' not in row.index or 'long_mavg' not in row.index:
        return 'hold'

    if row['short_mavg'] > row['long_mavg']:
        return 'buy'
    elif row['short_mavg'] < row['long_mavg']:
        return 'sell'
    else:
        return 'hold'

def momentum_strategy(row):
    """
    Momentum strategy function.
    
    Parameters:
    row (pd.Series): A row of historical price data.
    
    Returns:
    str: 'buy', 'sell', or 'hold' signal.
    """
    if 'returns' not in row.index:
        return 'hold'
    
    # Buy if returns are positive, sell if returns are negative
    if row['returns'] > 0:
        return 'buy'
    elif row['returns'] < 0:
        return 'sell'
    else:
        return 'hold'

def mean_reversion_strategy(row):
    """
    Mean reversion strategy function.
    
    Parameters:
    row (pd.Series): A row of historical price data.
    
    Returns:
    str: 'buy', 'sell', or 'hold' signal.
    """
    if 'z_score' not in row.index:
        return 'hold'
    
    # Buy if the z-score is less than -1 (indicating the price is lower than the average)
    # Sell if the z-score is greater than 1 (indicating the price is higher than the average)
    if row['z_score'] < -1:
        return 'buy'
    elif row['z_score'] > 1:
        return 'sell'
    else:
        return 'hold'

if __name__ == "__main__":
    # Example usage
    data = pd.read_csv('data/historical_data/btc_usd.csv', parse_dates=['Date'], index_col='Date')
    data.sort_values('Date', inplace=True)

    # Calculate moving averages for example strategy
    data['short_mavg'] = data['Close'].rolling(window=40, min_periods=1).mean()
    data['long_mavg'] = data['Close'].rolling(window=100, min_periods=1).mean()

    # Calculate returns for momentum strategy
    data['returns'] = data['Close'].pct_change().fillna(0)

    # Calculate z-score for mean reversion strategy
    data['rolling_mean'] = data['Close'].rolling(window=20).mean()
    data['rolling_std'] = data['Close'].rolling(window=20).std()
    data['z_score'] = (data['Close'] - data['rolling_mean']) / data['rolling_std']

    # Choose a strategy to run the backtest
    strategy = example_strategy  # Replace with momentum_strategy or mean_reversion_strategy as needed

    results = run_backtest(data, strategy)
    results.to_csv('results/backtest_results.csv', index=False)
    print(results.head())
