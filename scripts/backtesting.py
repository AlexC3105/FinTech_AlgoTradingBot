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
            'Date': row['Date'],
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
    if row['Close'] < row['Close'].rolling(window=20).mean():
        return 'buy'
    elif row['Close'] > row['Close'].rolling(window=20).mean():
        return 'sell'
    else:
        return 'hold'

if __name__ == "__main__":
    # Example usage
    data = pd.read_csv('data/historical_data/btc_usd.csv', parse_dates=['Date'])
    data.sort_values('Date', inplace=True)
    results = run_backtest(data, example_strategy)
    results.to_csv('results/backtest_results.csv', index=False)
    print(results)
