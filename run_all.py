"""
run_all.py

## Purpose
The `run_all.py` file serves as the main execution script for the entire cryptocurrency analysis and prediction project. This script orchestrates the sequence of tasks, from data preparation to model training, evaluation, backtesting, and report generation. By running this single script, users can ensure that all necessary steps are performed in the correct order, leading to a comprehensive analysis and prediction workflow.

## Importance
Automating the entire workflow through a single script offers several benefits:
1. **Consistency**: Ensures that all steps are executed in the correct sequence, reducing the risk of errors.
2. **Efficiency**: Saves time by automating the execution of multiple notebooks and scripts, allowing users to focus on analysis and strategy development.
3. **Reproducibility**: Facilitates the reproduction of results by providing a clear and automated process for executing the project.

## Functionality
1. **Data Preparation**:
   - Executes the data preparation notebook to preprocess the raw cryptocurrency data.
   
2. **Data Analysis**:
   - Runs the data analysis notebook to explore and visualize the historical data.
   
3. **Model Training**:
   - Executes the model training notebooks to build and train both the LSTM and random forest models.
   
4. **Prediction Generation**:
   - Runs the prediction generation notebooks to generate future price predictions using the trained models.
   
5. **Backtesting**:
   - Executes the backtesting script to evaluate the performance of trading strategies based on historical data.
   
6. **Report Generation**:
   - Runs the report generation script to compile the analysis results, backtesting performance, and future predictions into comprehensive reports.

## Example Usage
```python
python run_all.py

"""



import subprocess
import os
import curses

def run_notebook(notebook_path):
    """
    Execute a Jupyter notebook using nbconvert.
    
    Args:
        notebook_path (str): The path to the notebook file to execute.
    """
    print(f"Running notebook: {notebook_path}")
    result = subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', '--inplace', notebook_path])
    if result.returncode != 0:
        raise Exception(f"Error executing notebook {notebook_path}")

def run_script(script_path, *args):
    """
    Execute a Python script with arguments.
    
    Args:
        script_path (str): The path to the Python script to execute.
        args: Additional arguments to pass to the script.
    """
    command = ['python', script_path] + list(args)
    print(f"Running script: {' '.join(command)}")
    result = subprocess.run(command)
    if result.returncode != 0:
        raise Exception(f"Error executing script {' '.join(command)}")

def curses_menu(stdscr, prompt, options):
    """
    Display a menu using curses and allow the user to select an option with arrow keys.
    
    Args:
        stdscr: The curses window object.
        prompt (str): The prompt message to display.
        options (list): A list of options to display.
    
    Returns:
        str: The selected option.
    """
    current_row = 0

    def print_menu():
        stdscr.clear()
        stdscr.addstr(1, 2, prompt)
        for idx, row in enumerate(options):
            x = 2  # Fixed position to align text to the left
            y = idx + 3  # Offset for menu items
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
        stdscr.refresh()

    curses.curs_set(0)
    stdscr.keypad(1)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    print_menu()
    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return options[current_row]
        print_menu()

def main(stdscr):
    try:
        # Select cryptocurrency
        cryptos = ['BTC - []', 'ETH - []', 'SOL - []', 'ALL - []']
        crypto_prompt = "Please choose a cryptocurrency:"
        crypto = curses_menu(stdscr, crypto_prompt, cryptos)
        crypto = crypto.split(" ")[0]
        
        # Pull and clean data
        stdscr.clear()
        stdscr.addstr(2, 2, f"Pulling and cleaning data for {crypto}...")
        stdscr.refresh()
        run_script('scripts/select_crypto_and_pull_data.py', '--crypto', crypto)
        
        # Data Preparation
        stdscr.clear()
        stdscr.addstr(2, 2, "Running data preparation notebook...")
        stdscr.refresh()
        run_notebook('notebooks/01_data_preparation.ipynb')
        
        # Data Analysis
        stdscr.clear()
        stdscr.addstr(2, 2, "Running data analysis notebook...")
        stdscr.refresh()
        run_notebook('notebooks/02_data_analysis.ipynb')
        
        # Model Training
        stdscr.clear()
        stdscr.addstr(2, 2, "Running model generation notebook...")
        stdscr.refresh()
        run_notebook('notebooks/03_model_generation.ipynb')
        
        # Prediction Generation
        stdscr.clear()
        stdscr.addstr(2, 2, "Running prediction generation notebook...")
        stdscr.refresh()
        run_notebook('notebooks/04_prediction_generation.ipynb')
        
        # Backtesting
        stdscr.clear()
        stdscr.addstr(2, 2, "Running backtesting notebook...")
        stdscr.refresh()
        run_notebook('notebooks/05_backtesting.ipynb')
        
        # Select strategy
        strategies = ['STRAT - 1 []', 'STRAT - 2 []', 'STRAT - 3 []']
        strategy_prompt = "Please choose a desired strategy:"
        strategy = curses_menu(stdscr, strategy_prompt, strategies)
        strategy = strategy.split(" ")[1]
        
        # Select investment amount
        amounts = ['$100 - []', '$500 - []', '$1000 - []']
        amount_prompt = "Please select an amount:"
        amount = curses_menu(stdscr, amount_prompt, amounts)
        amount = amount.split(" ")[0]
        
        # Run backtesting with selected strategy and amount
        stdscr.clear()
        stdscr.addstr(2, 2, f"Running backtesting for {crypto} with strategy {strategy} and investment amount {amount}...")
        stdscr.refresh()
        run_script('scripts/backtesting.py', '--crypto', crypto, '--strategy', strategy, '--amount', amount)
        
        # Report Generation
        stdscr.clear()
        stdscr.addstr(2, 2, "Running report generation script...")
        stdscr.refresh()
        run_script('scripts/generate_report.py')
        
        stdscr.clear()
        stdscr.addstr(2, 2, "All steps executed successfully.")
        stdscr.refresh()
        stdscr.getch()  # Wait for user to see the message
        
    except Exception as e:
        stdscr.clear()
        stdscr.addstr(2, 2, f"An error occurred: {e}")
        stdscr.refresh()
        stdscr.getch()  # Wait for user to see the message

if __name__ == "__main__":
    curses.wrapper(main)
