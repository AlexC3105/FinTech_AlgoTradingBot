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

def run_notebook(stdscr, notebook_path):
    """
    Execute a Jupyter notebook using nbconvert and display output in the curses window.
    
    Args:
        stdscr: The curses window object.
        notebook_path (str): The path to the notebook file to execute.
    """
    jupyter_path = "/opt/anaconda3/bin/jupyter"  # Actual path to the jupyter executable
    stdscr.addstr(f"Running notebook: {notebook_path[:curses.COLS-1]}\n")
    stdscr.refresh()
    result = subprocess.run([jupyter_path, 'nbconvert', '--to', 'notebook', '--execute', '--inplace', notebook_path], capture_output=True, text=True)
    output_lines = result.stdout.split('\n')
    for line in output_lines:
        stdscr.addstr(line[:curses.COLS-1] + '\n')
        stdscr.refresh()
    if result.returncode != 0:
        error_lines = result.stderr.split('\n')
        for line in error_lines:
            stdscr.addstr(line[:curses.COLS-1] + '\n')
            stdscr.refresh()
        raise Exception(f"Error executing notebook {notebook_path}: {result.stderr}")

def run_script(stdscr, script_path, *args):
    """
    Execute a Python script with arguments and display output in the curses window.
    
    Args:
        stdscr: The curses window object.
        script_path (str): The path to the Python script to execute.
        args: Additional arguments to pass to the script.
    """
    command = ['python', script_path] + list(args)
    stdscr.addstr(f"Running script: {' '.join(command)[:curses.COLS-1]}\n")
    stdscr.refresh()
    result = subprocess.run(command, capture_output=True, text=True)
    output_lines = result.stdout.split('\n')
    for line in output_lines:
        stdscr.addstr(line[:curses.COLS-1] + '\n')
        stdscr.refresh()
    if result.returncode != 0:
        error_lines = result.stderr.split('\n')
        for line in error_lines:
            stdscr.addstr(line[:curses.COLS-1] + '\n')
            stdscr.refresh()
        raise Exception(f"Error executing script {' '.join(command)}: {result.stderr}")

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
        stdscr.addstr(1, 2, prompt[:curses.COLS-1])
        for idx, row in enumerate(options):
            x = 2  # Fixed position to align text to the left
            y = idx + 3  # Offset for menu items
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row[:curses.COLS-1])
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row[:curses.COLS-1])
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

def run_controller_notebook(stdscr, crypto):
    """
    Run the controller notebook with the selected cryptocurrency.
    
    Args:
        stdscr: The curses window object.
        crypto (str): The selected cryptocurrency.
    """
    jupyter_path = "/opt/anaconda3/bin/jupyter"  # Actual path to the jupyter executable
    stdscr.addstr(f"Running controller notebook for {crypto}\n")
    stdscr.refresh()
    result = subprocess.run([jupyter_path, 'nbconvert', '--to', 'notebook', '--execute', '--inplace', 'notebooks/controller.ipynb'], capture_output=True, text=True, env={'CRYPTO': crypto})
    output_lines = result.stdout.split('\n')
    for line in output_lines:
        stdscr.addstr(line[:curses.COLS-1] + '\n')
        stdscr.refresh()
    if result.returncode != 0:
        error_lines = result.stderr.split('\n')
        for line in error_lines:
            stdscr.addstr(line[:curses.COLS-1] + '\n')
            stdscr.refresh()
        raise Exception(f"Error executing controller notebook for {crypto}: {result.stderr}")

def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(1)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    try:
        # Select cryptocurrency
        cryptos = ['BTC - []', 'ETH - []', 'SOL - []', 'ALL - []']
        crypto_prompt = "Please choose a cryptocurrency:"
        crypto = curses_menu(stdscr, crypto_prompt, cryptos)
        crypto = crypto.split(" ")[0]
        
        if crypto == "ALL":
            # Fetch data for all cryptocurrencies
            stdscr.clear()
            stdscr.addstr(2, 2, "Fetching data for all cryptocurrencies...\n")
            stdscr.refresh()
            run_script(stdscr, 'scripts/select_crypto_and_pull_data.py', '--crypto', 'ALL')
            # Run all notebooks if "ALL" is selected
            notebooks = [
                'notebooks/01_data_preparation.ipynb',
                'notebooks/02_data_analysis.ipynb',
                'notebooks/03_model_generation.ipynb',
                'notebooks/04_prediction_generation.ipynb',
                'notebooks/05_backtesting.ipynb',
                'notebooks/06_visualization.ipynb',
                'notebooks/lstm_neural_network.ipynb',
                'notebooks/lstm_nn_predict.ipynb',
                'notebooks/random_forest_model.ipynb',
                'notebooks/rf_predict.ipynb'
            ]
            for notebook in notebooks:
                stdscr.clear()
                stdscr.addstr(2, 2, f"Running {notebook[:curses.COLS-1]}...\n")
                stdscr.refresh()
                run_notebook(stdscr, notebook)
        else:
            # Fetch data for selected cryptocurrency
            stdscr.clear()
            stdscr.addstr(2, 2, f"Fetching data for {crypto}\n")
            stdscr.refresh()
            run_script(stdscr, 'scripts/select_crypto_and_pull_data.py', '--crypto', crypto)
            
            # Run controller notebook
            stdscr.clear()
            stdscr.addstr(2, 2, f"Running controller notebook for {crypto}\n")
            stdscr.refresh()
            run_controller_notebook(stdscr, crypto)
        
        # Report Generation
        stdscr.clear()
        stdscr.addstr(2, 2, "Running report generation script...\n")
        stdscr.refresh()
        run_script(stdscr, 'scripts/generate_report.py')
        
        stdscr.clear()
        stdscr.addstr(2, 2, "All steps executed successfully.\n")
        stdscr.refresh()
        stdscr.getch()  # Wait for user to see the message
        
    except Exception as e:
        stdscr.clear()
        stdscr.addstr(2, 2, f"An error occurred: {str(e)[:curses.COLS-1]}\n")
        stdscr.refresh()
        stdscr.getch()  # Wait for user to see the message

if __name__ == "__main__":
    curses.wrapper(main)