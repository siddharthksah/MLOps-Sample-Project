import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from model.pipeline.model import create_pipeline

def load_latest_data():
    return pd.read_csv('data/raw/boston_housing.csv')

def main():
    # Load the latest dataset
    data = load_latest_data()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

    # Train the model
    pipeline = create_pipeline()

    # Start an MLflow run
    with mlflow.start_run():
        pipeline.fit(X_train, y_train)

        # Evaluate the model
        score = pipeline.score(X_test, y_test)
        print("Model accuracy:", score)

        # Log model metrics to MLflow
        mlflow.log_metric("accuracy", score)

        # Save the trained model
        mlflow.sklearn.log_model(pipeline, "model")

if __name__ == "__main__":
    main()
