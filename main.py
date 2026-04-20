from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

class Irisrequest(BaseModel):
    features: list[float]

# load the model 
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "Iris Classifier API is running"}

@app.post("/predict")
def predict(data: Irisrequest):
    features = np.array(data.features).reshape(1, -1)
    predictions = model.predict(features)

    return {
        "Prediction": int(predictions[0])
    }