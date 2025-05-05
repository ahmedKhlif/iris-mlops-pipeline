# MLOps Pipeline for Iris Classification

Ce projet met en place un pipeline MLOps complet pour la classification des fleurs d'Iris avec un RandomForestClassifier.

## Installation

```bash
# Windows
python -m venv mlops_env
mlops_env\Scripts\activate
pip install -r requirements.txt

# Unix/Mac
python3 -m venv mlops_env
source mlops_env/bin/activate
pip install -r requirements.txt
```

## Utilisation

1. Entraînez le modèle: `python train_model.py`
2. Lancez l'API: `uvicorn api:app --reload`
3. Testez l'API: `curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"features\":[5.1,3.5,1.4,0.2]}"`
4. Monitoring: `python monitoring.py`
5. Docker: `docker build -t ml-api .` puis `docker run -p 8001:8000 ml-api` 