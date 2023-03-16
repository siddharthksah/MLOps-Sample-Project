import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn

import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='_distutils_hack')



# Load your dataset
def load_data():
    # Load the Boston Housing dataset from the specified location
    data = pd.read_csv("data/raw/boston_housing.csv")
    return data

# Preprocess the data
def preprocess_data(data):
    # Assume the target variable is named 'target' in the dataset
    X = data.drop("medv", axis=1)
    y = data["medv"]
    return X, y

# Train the model
def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return mse

def main():
    # Load and preprocess the data
    data = load_data()
    X, y = preprocess_data(data)

    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    mse = evaluate_model(model, X_test, y_test)
    print(f"Mean Squared Error: {mse}")

    # Log the model with MLflow
    with mlflow.start_run() as run:
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, "model")
        
        # Get the run_id
        run_id = run.info.run_id
        print(f"Run ID: {run_id}")

        # Save the run_id to a file
        with open("run_id.txt", "w") as f:
            f.write(run_id)

if __name__ == "__main__":
    main()
