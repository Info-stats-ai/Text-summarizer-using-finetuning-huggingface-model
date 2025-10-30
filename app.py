from fastapi import FastAPI, Request, Body, Query
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.responses import Response
from pydantic import BaseModel
from src.textsummarization.pipeline.prediction_pipeline import PredictionPipeline
from src.textsummarization.logging import logger
from typing import Optional

text:str = "What is the Text Summarization?"
app = FastAPI()

class TextInput(BaseModel):
    text: str

class PredictOptions(BaseModel):
    text: str
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    num_beams: Optional[int] = None
    length_penalty: Optional[float] = None
    num_sentences: Optional[int] = None

templates = Jinja2Templates(directory="templates")

@app.get("/", tags=["authentication"])
async def index():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.get("/docs", tags=["authentication"])
async def docs():
    # Avoid redirect loop by sending users to ReDoc (or FastAPI's default docs at /docs if preferred)
    return RedirectResponse(url="/redoc")

@app.get("/train")
async def train():
    try:
        os.system("python main.py")
        return Response("Training successful!!")
        print("Training successful!!")
    except Exception as e:
        return Response(f"Error: {e}")
    
@app.api_route("/predict", methods=["GET", "POST"])
async def predict_route(
    request: Request,
    text: str | None = Query(default=None),
    payload: PredictOptions | None = Body(default=None),
):
    try:
        # Debug: request metadata
        logger.debug(f"/predict called: method={request.method}")
        logger.debug(f"content-type={request.headers.get('content-type')}")
        logger.debug(f"query_param_text_present={'yes' if text else 'no'}")

        # Determine payload from query or JSON body
        payload_text = None
        if request.method == "GET":
            logger.debug("Using text from query param (GET)")
            payload_text = text
        else:
            # Prefer JSON body {"text": "..."}
            if payload and payload.text:
                logger.debug("Using text from JSON body")
                payload_text = payload.text
            else:
                # try form data as a fallback
                if request.headers.get("content-type", "").startswith("application/x-www-form-urlencoded"):
                    logger.debug("Attempting to read text from form data")
                    form = await request.form()
                    payload_text = form.get("text")
                    logger.debug(f"form_text_present={'yes' if payload_text else 'no'}")
                # finally, fall back to query param
                if not payload_text:
                    logger.debug("Falling back to query param text on POST")
                    payload_text = text

        if not payload_text:
            return {"error": "Missing 'text' parameter in query string or JSON body"}

        logger.info(f"Received prediction request for text (first 100): {payload_text[:100]}...")
        logger.debug(f"Final payload_text_len={len(payload_text)}")
        obj = PredictionPipeline()
        # Collect optional generation controls
        opts = {}
        if payload:
            opts = {
                "min_length": payload.min_length,
                "max_length": payload.max_length,
                "num_beams": payload.num_beams,
                "length_penalty": payload.length_penalty,
                "num_sentences": payload.num_sentences,
            }
        result = obj.predict(payload_text, **{k: v for k, v in opts.items() if v is not None})
        logger.info("Prediction completed successfully")
        return result
    except Exception as e:
        logger.error(f"Error in prediction: {str(e)}")
        return {"error": f"Failed to generate summary: {str(e)}"}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)