import os

from fastapi import FastAPI, Query
from pydantic import BaseModel

from src.components.data_ingestion_config import DataIngestionConfig
from src.pipeline.prediction import custom_final_df
from src.utils import load_object

# Initialize FastAPI app
app = FastAPI()

# Load the model
ingestiConfig = DataIngestionConfig()
pkl_file_path = ingestiConfig.pkl_file_path
model = load_object(pkl_file_path)

# Request model for input validation
class URLRequest(BaseModel):
    url: str

@app.get("/")
def home():
    return {"message": "Phishing Domain Detection API is running!"}

@app.post("/predict/")
def predict(data: URLRequest):
    """
    Predict if the given URL is phishing or safe.
    """
    custom_data = custom_final_df(data.url)
    df = custom_data.final_df()
    
    prediction = model.predict(df)
    result = "Phishing Site" if prediction[0] == 1 else "Safe Site"

    return {"url": data.url, "prediction": result}


print("Checking pickle file existence:", os.path.exists(pkl_file_path))

