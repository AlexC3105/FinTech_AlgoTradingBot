"""
generate_report.py

## Purpose
The `generate_report.py` file is designed to automate the process of generating comprehensive reports for the algorithmic trading project. This script compiles analysis results, backtesting performance, and future predictions into a single, cohesive report. By automating report generation, we ensure that stakeholders receive consistent and up-to-date information about the project's performance.

## Importance
Automated report generation is crucial for several reasons:
1. **Consistency**: Ensures that all reports follow the same format and include the same key metrics and visualizations.
2. **Efficiency**: Saves time by automating the compilation of data and generation of reports, allowing team members to focus on analysis and strategy development.
3. **Communication**: Provides clear and detailed reports to stakeholders, making it easier to communicate the project's progress and results.

## Functionality
1. **Data Compilation**:
   - The script collects data from various sources, including historical data, backtesting results, and future predictions.
   
2. **Report Generation**:
   - Generates a report in a specified format (e.g., PDF, HTML) that includes key metrics, visualizations, and analysis results.
   
3. **Automation**:
   - Automates the entire process, from data collection to report generation, ensuring that the latest information is always included in the reports.

## Example Usage
```python
from scripts.generate_report import generate_report

# Generate a report for Bitcoin
generate_report('BTC')

# Generate a report for Ethereum
generate_report('ETH')

"""



import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

def generate_report(crypto):
    try:
        # Paths to required data and results
        data_path = f'data/cleaned_data/{crypto}_cleaned.csv'
        backtest_path = f'results/backtest_results_{crypto}.csv'
        prediction_path = f'results/nn_predictions_{crypto}.csv'
        report_path = f'reports/{crypto}_report.pdf'

        # Check if files exist
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"{data_path} does not exist")
        if not os.path.exists(backtest_path):
            raise FileNotFoundError(f"{backtest_path} does not exist")
        if not os.path.exists(prediction_path):
            raise FileNotFoundError(f"{prediction_path} does not exist")

        # Load data
        data = pd.read_csv(data_path, index_col='Date', parse_dates=True)
        backtest_results = pd.read_csv(backtest_path, index_col='Date', parse_dates=True)
        predictions = pd.read_csv(prediction_path, index_col='Date', parse_dates=True)

        # Create plots
        plt.figure(figsize=(14, 7))
        plt.plot(data['close'], label='Historical Prices')
        plt.plot(predictions.index, predictions['Predicted'], label='Predicted Prices', linestyle='--')
        plt.title(f'{crypto} Price Prediction')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plot_path = f'results/{crypto}_prediction_plot.png'
        plt.savefig(plot_path)
        plt.close()

        # Generate PDF report
        pdf = FPDF()
        pdf.add_page()

        # Title
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, f'{crypto} Analysis Report', 0, 1, 'C')

        # Historical Data Summary
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, 'Historical Data Summary', 0, 1)
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, data.describe().to_string())

        # Backtest Results
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, 'Backtest Results', 0, 1)
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, backtest_results.describe().to_string())

        # Prediction Plot
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, 'Prediction Plot', 0, 1)
        pdf.image(plot_path, x=10, y=None, w=190)

        # Save PDF
        os.makedirs('reports', exist_ok=True)
        pdf.output(report_path)
        print(f'Report generated: {report_path}')

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    cryptos = ['BTC', 'ETH', 'SOL']
    for crypto in cryptos:
        generate_report(crypto)