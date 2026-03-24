import joblib
import pandas as pd

model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

def predict(data):
    df = pd.DataFrame([data])
    df = df[features]
    return model.predict(df)[0]