"""
__init__.py

## Purpose
The `__init__.py` file is an essential component of the `scripts` module in our algorithmic trading project. This file allows the `scripts` directory to be treated as a Python package, enabling the import of various utility functions and classes defined within the module. By organizing our code into a package, we improve the structure and maintainability of the project, making it easier to manage and extend.

## Importance
Including an `__init__.py` file in the `scripts` directory provides several key benefits:
1. **Package Initialization**: It initializes the package and defines the modules that are available for import.
2. **Namespace Management**: It helps manage the namespace, preventing conflicts between different modules and ensuring that the correct functions are imported.
3. **Code Organization**: It improves code organization by allowing related functions and classes to be grouped into a single package, making the project more modular and maintainable.

## Functionality
1. **Package Initialization**:
   - The `__init__.py` file initializes the `scripts` package, making it possible to import functions and classes from this directory.
   
2. **Module Imports**:
   - The file imports key functions and classes from the various modules within the `scripts` package, providing a central point of access for these utilities.
   - This approach simplifies the import statements in other parts of the project, allowing for cleaner and more readable code.

## Example Usage
```python
from scripts import api_integration, backtesting, data_preparation

# Use functions from the scripts package
historical_data = api_integration.fetch_historical_data('BTC', '2020-01-01', '2021-01-01')
backtest_results = backtesting.run_backtest(historical_data, backtesting.example_strategy)
cleaned_data = data_preparation.clean_data(historical_data)

"""



from .api_integration import fetch_historical_data, fetch_real_time_data
from .backtesting import run_backtest, example_strategy
from .data_preparation import clean_data, preprocess_data

__all__ = [
    'fetch_historical_data',
    'fetch_real_time_data',
    'run_backtest',
    'example_strategy',
    'clean_data',
    'preprocess_data'
]
