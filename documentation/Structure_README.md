# Project Structure Overview

```
FinTech_AlgoTradingBot/
│
├── data/
│   ├── BTC-USD.csv
│   ├── ETH-USD.csv
│   ├── SOL-USD.csv
│   └── .ipynb_checkpoints/
│       └── BTC-USD-checkpoint.csv
│
├── cleaned_data/
│   ├── BTC_cleaned.csv
│   ├── ETH_cleaned.csv
│   ├── SOL_cleaned.csv
│
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   ├── 02_data_analysis.ipynb
│   ├── 03_model_generation.ipynb
│   ├── 04_prediction_generation.ipynb
│   ├── 05_backtesting.ipynb
│   ├── 06_visualization.ipynb
│   ├── controller.ipynb
│   ├── lstm_neural_network.ipynb
│   ├── lstm_nn_predict.ipynb
│   ├── main.ipynb
│   └── .ipynb_checkpoints/
│       ├── controller-checkpoint.ipynb
│       ├── data_analysis-checkpoint.ipynb
│       ├── data_prep-checkpoint.ipynb
│       ├── lstm_neural_network-checkpoint.ipynb
│       ├── lstm_nn_predict-checkpoint.ipynb
│       ├── main-checkpoint.ipynb
│       ├── neural_network-checkpoint.ipynb
│       └── neuralnet-checkpoint.ipynb
│
├── scripts/
│   ├── utils.py
│   ├── models.py
│   ├── interface.py
│   └── backtesting.py
│
├── results/
│   ├── output_predictions/
│   │   ├── btc_usd_predictions.csv
│   │   ├── eth_usd_predictions.csv
│   │   └── sol_usd_predictions.csv
│   └── visualizations/
│       ├── volatility_analysis.png
│       └── exchange_rate_trends.png
│
├── documentation/
│   ├── README.md
│   └── project_report.pdf
│
├── presentation/
│   └── Algo_Trading_Presentation.pptx
│
├── .env
├── .gitignore
├── requirements.txt
└── select_crypto_and_pull_data.py
```

# Explanation of Each Component

## data/ Directory
- **historical_data/**: This folder will store CSV files with historical data for different cryptocurrencies like Bitcoin, Ethereum, and Solana.
  - **BTC-USD.csv**: Historical data for Bitcoin to USD.
  - **ETH-USD.csv**: Historical data for Ethereum to USD.
  - **SOL-USD.csv**: Historical data for Solana to USD.

## cleaned_data/ Directory
- **BTC_cleaned.csv**: Cleaned data for Bitcoin to USD.
- **ETH_cleaned.csv**: Cleaned data for Ethereum to USD.
- **SOL_cleaned.csv**: Cleaned data for Solana to USD.

## notebooks/ Directory
- **01_data_preparation.ipynb**: This notebook focuses on cleaning and preprocessing the raw historical data.
  - **Inputs**: CSV files from the historical_data folder.
  - **Outputs**: Cleaned data ready for analysis, saved to the cleaned_data folder.
- **02_data_analysis.ipynb**: This notebook analyzes the historical data to uncover trends and insights.
  - **Inputs**: Cleaned data from the data preparation notebook.
  - **Outputs**: Analytical findings and possibly some initial visualizations.
- **03_model_generation.ipynb**: This notebook is where the trading models (e.g., machine learning models) are created and trained.
  - **Inputs**: Preprocessed data from the previous notebooks.
  - **Outputs**: Trained models, saved to the models folder.
- **04_prediction_generation.ipynb**: This notebook generates predictions for future exchange rates using the trained models.
  - **Inputs**: Trained models and potentially new data for making predictions.
  - **Outputs**: Prediction results saved in the output_predictions folder.
- **05_backtesting.ipynb**: This notebook tests the trading strategies using historical data to see how well they would have performed.
  - **Inputs**: Historical data and trading strategy logic.
  - **Outputs**: Backtesting results, saved to the results folder.
- **06_visualization.ipynb**: This notebook creates visualizations to help understand the data and model performance.
  - **Inputs**: Data and results from other notebooks.
  - **Outputs**: Visualizations saved in the visualizations folder.
- **controller.ipynb**: Manages the overall workflow and integrates various components of the project.
- **lstm_neural_network.ipynb**: Builds and trains an LSTM neural network for time series prediction.
- **lstm_nn_predict.ipynb**: Uses the trained LSTM model to make predictions.
- **main.ipynb**: Main notebook that ties all parts of the project together.

## scripts/ Directory
- **utils.py**: Contains utility functions used across different notebooks and scripts for tasks like data processing and manipulation.
- **models.py**: Defines the various trading algorithms and models used in the project.
- **interface.py**: A user interface script to make the tool more user-friendly, allowing users to interact with the models and data without diving into the code.
- **backtesting.py**: Contains logic for backtesting trading strategies to evaluate their performance using historical data.

## results/ Directory
- **output_predictions/**: Stores CSV files with the predicted exchange rates.
  - **btc_usd_predictions.csv**: Predictions for Bitcoin to USD.
  - **eth_usd_predictions.csv**: Predictions for Ethereum to USD.
  - **sol_usd_predictions.csv**: Predictions for Solana to USD.
- **visualizations/**: Stores the visualizations created during the project.
  - **volatility_analysis.png**: Visualization showing volatility analysis.
  - **exchange_rate_trends.png**: Visualization showing trends in exchange rates.

## documentation/ Directory
- **README.md**: Provides an overview of the project, setup instructions, and usage guidelines.
- **project_report.pdf**: A detailed report documenting the methodologies used and findings of the project.

## presentation/ Directory
- **Algo_Trading_Presentation.pptx**: A PowerPoint presentation summarizing the project, including key findings and methodologies.

## Other Important Files
- **.env**: Stores API keys and other environment variables needed for the project.
- **.gitignore**: Specifies which files and directories should be ignored by Git.
- **requirements.txt**: Lists all the Python dependencies required for the project.
- **select_crypto_and_pull_data.py**: Script for selecting a cryptocurrency and pulling the relevant data using the API keys stored in the .env file.

# Flow of Control

## Select and Pull Data:
- Use **select_crypto_and_pull_data.py** to choose a cryptocurrency and fetch its historical data, which gets saved in the data/historical_data/ folder.

## Data Preparation:
- Run **01_data_preparation.ipynb** to clean and preprocess the fetched data.

## Data Analysis:
- Analyze the cleaned data using **02_data_analysis.ipynb** to uncover trends and insights.

## Model Generation:
- Create and train trading models with **03_model_generation.ipynb** using the prepared data.

## Prediction Generation:
- Generate future exchange rate predictions with **04_prediction_generation.ipynb** using the trained models.

## Backtesting:
- Test the trading strategies with historical data using **05_backtesting.ipynb** to evaluate their performance.

## Visualization:
- Create visual representations of the data and results with **06_visualization.ipynb** for better understanding and communication.

## Documentation and Presentation:
- Update **README.md** and create a project report (**project_report.pdf**) to document the project's methodology and findings.
- Summarize the project in a presentation (**Algo_Trading_Presentation.pptx**) for sharing with stakeholders.

This structured approach ensures a systematic workflow from data collection to analysis, model development, and result presentation, facilitating clear and organized project management.
