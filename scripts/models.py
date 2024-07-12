"""
models.py

## Purpose
The `models.py` file is a critical component of our algorithmic trading project. It defines the machine learning models and trading algorithms that will be used to analyze historical cryptocurrency data and make future price predictions. This script encapsulates the logic for training, evaluating, and using these models, making it easier to develop and maintain our predictive models.

## Importance
Having a dedicated script for models is essential for several reasons:
1. **Modularity**: It separates the model-related code from other parts of the project, making the codebase more organized and maintainable.
2. **Reusability**: The functions defined in this script can be reused across different notebooks and scripts, promoting code reuse and reducing duplication.
3. **Scalability**: It allows us to easily add, modify, and test different models and algorithms as the project evolves.
4. **Consistency**: It ensures that the models are trained and evaluated in a consistent manner, which is crucial for reliable performance assessment.

## Functionality
1. **Train Model**:
   - The `train_model` function is responsible for training a machine learning model on the historical data.
   - It splits the data into training and testing sets, trains the model, and returns the trained model along with the test data.
   
2. **Make Prediction**:
   - The `make_prediction` function uses a trained model to make predictions on new data.
   - It takes the model and the data as inputs and returns the predicted values.

3. **Model Definitions**:
   - The script defines specific models, such as Random Forest, which can be used for making predictions based on historical data.

## Example Usage
### Train Model
```python
import pandas as pd
from scripts.models import train_model
import joblib

# Load preprocessed data
data_path = 'data/historical_data/btc_usd_preprocessed.csv'  # Update this path based on the selected cryptocurrency
data = pd.read_csv(data_path, parse_dates=['Date'], index_col='Date')

# Train model
model, X_test, y_test = train_model(data)

# Save the model and test data
joblib.dump(model, 'models/trained_model.pkl')
X_test.to_csv('data/historical_data/X_test.csv')
y_test.to_csv('data/historical_data/y_test.csv')

# Display model performance
print(f"Model trained. R^2 score on training data: {model.score(X_test, y_test)}")

"""



from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import joblib

def train_model(data, features):
    """
    Train a machine learning model on historical data.
    
    Parameters:
    data (pd.DataFrame): Historical price data.
    features (list): List of feature column names.
    
    Returns:
    model: Trained machine learning model.
    X_test: Test features.
    y_test: Test labels.
    """
    data = data.dropna()  # Drop any rows with missing values
    X = data[features]
    y = data['Close'].shift(-1).dropna()
    X = X[:-1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    return model, X_test, y_test

def make_prediction(model, data, features):
    """
    Make predictions using the trained model.
    
    Parameters:
    model: Trained machine learning model.
    data (pd.DataFrame): Data to make predictions on.
    features (list): List of features to use for prediction.
    
    Returns:
    pd.Series: Predicted values.
    """
    X = data[features]
    predictions = model.predict(X)
    return pd.Series(predictions, index=data.index)

if __name__ == "__main__":
    features = ['Open', 'High', 'Low', 'Volume']
    data = pd.read_csv('data/historical_data/btc_usd.csv', parse_dates=['Date'], index_col='Date')
    
    model, X_test, y_test = train_model(data, features)
    predictions = make_prediction(model, data, features)
    
    # Save the model and test data
    joblib.dump(model, 'models/trained_model.pkl')
    X_test.to_csv('data/historical_data/X_test.csv')
    y_test.to_csv('data/historical_data/y_test.csv')
    
    # Save predictions
    results = data[['Close']].copy()
    results['Predictions'] = predictions
    results.to_csv('results/predictions.csv', index=True)
    
    print("Model trained and predictions saved.")
    print(results.head())
