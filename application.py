from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.responses import Response
from pydantic import BaseModel
from src.textsummarization.pipeline.prediction_pipeline import PredictionPipeline
from src.textsummarization.logging import logger

text:str = "What is the Text Summarization?"
application = FastAPI()

class TextInput(BaseModel):
    text: str

templates = Jinja2Templates(directory="templates")

@application.get("/", tags=["authentication"])
async def index():
    return templates.TemplateResponse("index.html", {"request": {}})

@application.get("/docs", tags=["authentication"])
async def docs():
    return RedirectResponse(url="/docs")

@application.get("/train")
async def train():
    try:
        os.system("python main.py")
        return Response("Training successful!!")
    except Exception as e:
        return Response(f"Error: {e}")
    
@application.post("/predict")
async def predict_route(text: str):
    try:
        logger.info(f"Received prediction request for text: {text[:100]}...")
        obj = PredictionPipeline()
        summary = obj.predict(text)
        logger.info("Prediction completed successfully")
        return summary
    except Exception as e:
        logger.error(f"Error in prediction: {str(e)}")
        return f"Error: Failed to generate summary. {str(e)}"
    
if __name__ == "__main__":
    uvicorn.run(application, host="0.0.0.0", port=8080)