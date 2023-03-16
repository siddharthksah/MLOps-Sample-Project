import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from model.pipeline.model import create_pipeline

def load_latest_data():
    return pd.read_csv('data/raw/boston_housing.csv')

def main():
    # Load the latest dataset
    data = load_latest_data()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

    # Load the trained model
    pipeline = create_pipeline()
    pipeline.fit(X_train, y_train)

    # Make predictions
    y_pred = pipeline.predict(X_test)

    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Mean Squared Error:", mse)
    print("R2 Score:", r2)

if __name__ == "__main__":
    main()
