from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from model.pipeline.preprocessors import CustomPreprocessor

def create_pipeline():
    preprocessor = CustomPreprocessor()
    model = LinearRegression()
    
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('model', model),
    ])

    return pipeline
