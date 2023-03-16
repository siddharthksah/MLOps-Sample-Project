from flask import Flask
import mlflow
import mlflow.sklearn
from app.core.config import Config
from app.api.endpoints.predictions import predictions

app = Flask(__name__)
app.config.from_object(Config)

# Load the model from MLflow
model = mlflow.sklearn.load_model("runs:/<run_id>/model")

app.register_blueprint(predictions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
