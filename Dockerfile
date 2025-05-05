FROM python:3.10.11

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY api.py .
COPY model.pkl .
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"] 