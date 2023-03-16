import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

import mlflow.pyfunc
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

def load_model():
    # Read the run_id from the file
    with open("run_id.txt", "r") as f:
        run_id = f.read().strip()

    # Load the model using the run_id
    model_uri = f"runs:/{run_id}/model"
    model = mlflow.pyfunc.load_model(model_uri)
    return model

# Load the latest trained model
model = load_model()

@app.route("/predict", methods=["POST"])
def predict():
    # Read input JSON data
    input_data = request.json

    # Convert the input JSON data to a DataFrame
    input_df = pd.DataFrame(input_data)

    # Make predictions
    predictions = model.predict(input_df)

    # Convert the predictions to a list
    predictions_list = predictions.tolist()

    return jsonify(predictions_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
