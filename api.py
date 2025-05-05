from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Charger le modèle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Route GET pour vérifier si l'API fonctionne
@app.get("/")
def home():
    return {"message": "API MLOps fonctionne !"}

# Définition des données d'entrée pour la prédiction
class InputData(BaseModel):
    features: list

# Route POST pour effectuer des prédictions
@app.post("/predict")
def predict(data: InputData):
    prediction = model.predict(np.array(data.features).reshape(1, -1))
    return {"prediction": int(prediction[0])} 