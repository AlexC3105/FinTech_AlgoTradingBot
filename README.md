# FinTech_AlgoTradingBot
FinTech_AlgoTradingBot is an algorithmic trading bot developed as part of a FinTech Bootcamp project. This project focuses on creating an automated trading solution tailored for small businesses, startups, tech enthusiasts, and cryptocurrency investors interested in algorithmic trading strategies.

## Project Structure Overview

```
FinTech_AlgoTradingBot/
│
├── data/
│   ├── cleaned_data/               # Cleaned and preprocessed data
│   ├── historical_data/            # Raw historical data
│
├── models/                         # Trained models and scalers
│   ├── BTC_lstm_model.h5
│   ├── BTC_scaler.pkl
│   ├── ETH_lstm_model.h5
│   ├── ETH_scaler.pkl
│   ├── SOL_lstm_model.h5
│   ├── SOL_scaler.pkl
│   └── ...                         # Other models and related files
│
├── notebooks/                      # Jupyter notebooks for various stages
│   ├── 01_data_preparation.ipynb
│   ├── 02_data_analysis.ipynb
│   ├── 03_model_generation.ipynb
│   ├── 04_prediction_generation.ipynb
│   ├── 05_backtesting.ipynb
│   ├── 06_visualization.ipynb
│   ├── controller.ipynb
│   ├── main.ipynb
│   └── ...                         # Other notebooks and checkpoint files
│
├── results/                        # Results of the analysis and predictions
│   ├── output_predictions/         # Output predictions
│
├── scripts/                        # Python scripts for various functionalities
│   ├── __init__.py
│   ├── api_integration.py
│   ├── backtesting.py
│   └── generate_report.py
│
├── README.md                       # Project description and instructions
├── LICENSE                         # License for the project
├── requirements.txt                # Required Python packages
├── run_all.py                      # Main script to run the entire workflow
├── .gitignore                      # Git ignore file
└── ...                             # Other project files
```
# Explanation of Each Component

## data/ Directory
- **cleaned_data/**: Cleaned and preprocessed data
- **historical_data/**: Raw historical data

## models/ Directory
- **BTC_lstm_model.h5**: Trained LSTM model for Bitcoin
- **BTC_scaler.pkl**: Scaler for Bitcoin data
- **ETH_lstm_model.h5**: Trained LSTM model for Ethereum
- **ETH_scaler.pkl**: Scaler for Ethereum data
- **SOL_lstm_model.h5**: Trained LSTM model for Solana
- **SOL_scaler.pkl**: Scaler for Solana data
- **...**: Other models and related files

## notebooks/ Directory
- **01_data_preparation.ipynb**: This notebook focuses on cleaning and preprocessing the raw historical data.
  - **Inputs**: CSV files from the historical_data folder.
  - **Outputs**: Cleaned data ready for analysis, which might be saved back to the historical_data folder or another location.
- **02_data_analysis.ipynb**: This notebook analyzes the historical data to uncover trends and insights.
  - **Inputs**: Cleaned data from the data preparation notebook.
  - **Outputs**: Analytical findings and possibly some initial visualizations.
- **03_model_generation.ipynb**: This notebook is where the trading models (e.g., machine learning models) are created and trained.
  - **Inputs**: Preprocessed data from the previous notebooks.
  - **Outputs**: Trained models, which might be saved to the models folder.
- **04_prediction_generation.ipynb**: This notebook generates predictions for future exchange rates using the trained models.
  - **Inputs**: Trained models and potentially new data for making predictions.
  - **Outputs**: Prediction results saved in the output_predictions folder.
- **05_backtesting.ipynb**: This notebook tests the trading strategies using historical data to see how well they would have performed.
  - **Inputs**: Historical data and trading strategy logic.
  - **Outputs**: Backtesting results, which might be saved to the results folder.
- **06_visualization.ipynb**: This notebook creates visualizations to help understand the data and model performance.
  - **Inputs**: Data and results from other notebooks.
  - **Outputs**: Visualizations saved in the visualizations folder.
- **controller.ipynb**: Notebook to control the flow of operations.
- **main.ipynb**: Main notebook to interact with the project.

## results/ Directory
- **output_predictions/**: Stores the output predictions.

## scripts/ Directory
- **init.py**: Initialization file for the scripts package.
- **api_integration.py**: Script for integrating with various APIs.
- **backtesting.py**: Script for backtesting trading strategies.
- **generate_report.py**: Script for generating reports.

## Other Important Files
- **README.md**: Project description and instructions.
- **LICENSE**: License for the project.
- **requirements.txt**: Required Python packages.
- **run_all.py**: Main script to run the entire workflow.
- **.gitignore**: Specifies which files and directories should be ignored by Git.

# Flow of Control

## Select and Pull Data:
Use **select_crypto_and_pull_data.py** to choose a cryptocurrency and fetch its historical data, which gets saved in the data/historical_data/ folder.

## Data Preparation:
Run **01_data_preparation.ipynb** to clean and preprocess the fetched data.

## Data Analysis:
Analyze the cleaned data using **02_data_analysis.ipynb** to uncover trends and insights.

## Model Generation:
Create and train trading models with **03_model_generation.ipynb** using the prepared data.

## Prediction Generation:
Generate future exchange rate predictions with **04_prediction_generation.ipynb** using the trained models.

## Backtesting:
Test the trading strategies with historical data using **05_backtesting.ipynb** to evaluate their performance.

## Visualization:
Create visual representations of the data and results with **06_visualization.ipynb** for better understanding and communication.

## Documentation and Presentation:
Update **README.md** and create a project report (**project_report.pdf**) to document the project's methodology and findings.
Summarize the project in a presentation (**Algo_Trading_Presentation.pptx**) for sharing with stakeholders.

# Instalation and Setup

## Cloning the Repository and Setting Up:
Follow these instructions to clone the repository, install dependencies, and set up the environment for the project.

## Clone the Repository:
```
git clone git@github.com:AlexC3105/FinTech_AlgoTradingBot.git
cd FinTech_AlgoTradingBot
```

## Install Dependencies:
Make sure you have Python 3.8 or above installed. Then, install the required packages using pip:
```
pip install -r requirements.txt
```

## Add .env file:
Create a .env file in the root directory of the project and add your API keys. The file should look like this:
```
ALPACA_API_KEY=your_alpaca_api_key
ALPACA_SECRET_KEY=your_alpaca_secret_key
YAHOO_FINANCE_API_KEY=your_yahoo_finance_api_key
```

## Running the Project:
Navigate to the project directory and run the main script to start the entire workflow:
```
cd FinTech_AlgoTradingBot
python run_all.py
```
These commands will set up the project and start the algorithmic trading bot. Ensure that you replace placeholder values in the .env file with your actual API keys.
