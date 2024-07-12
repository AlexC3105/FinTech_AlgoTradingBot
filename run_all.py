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

def run_notebook(notebook_path):
    """
    Execute a Jupyter notebook using nbconvert.
    
    Args:
        notebook_path (str): The path to the notebook file to execute.
    """
    result = subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', '--inplace', notebook_path])
    if result.returncode != 0:
        raise Exception(f"Error executing notebook {notebook_path}")

def run_script(script_path):
    """
    Execute a Python script.
    
    Args:
        script_path (str): The path to the Python script to execute.
    """
    result = subprocess.run(['python', script_path])
    if result.returncode != 0:
        raise Exception(f"Error executing script {script_path}")

def main():
    try:
        # Data Preparation
        print("Running data preparation notebook...")
        run_notebook('notebooks/01_data_preparation.ipynb')
        
        # Data Analysis
        print("Running data analysis notebook...")
        run_notebook('notebooks/02_data_analysis.ipynb')
        
        # Model Training
        print("Running model generation notebook...")
        run_notebook('notebooks/03_model_generation.ipynb')
        
        # Prediction Generation
        print("Running prediction generation notebook...")
        run_notebook('notebooks/04_prediction_generation.ipynb')
        
        # Backtesting
        print("Running backtesting notebook...")
        run_notebook('notebooks/05_backtesting.ipynb')
        
        # Report Generation
        print("Running report generation script...")
        run_script('scripts/generate_report.py')
        
        print("All steps executed successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
