from src.textsummarization.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline
from src.textsummarization.logging import logger

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text):
        try:
            logger.info(f"Loading tokenizer from: {self.config.tokenizer_path}")
            tokenizer = AutoTokenizer.from_pretrained(str(self.config.tokenizer_path))
            
            logger.info(f"Loading model from: {self.config.model_path}")
            
            # Dynamic max_length based on input length
            input_length = len(text.split())
            if input_length < 50:
                max_length = min(32, input_length // 2)
            elif input_length < 200:
                max_length = 64
            else:
                max_length = 128
                
            gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": max_length}
          
            pipe = pipeline("summarization", model=str(self.config.model_path), tokenizer=tokenizer)
            
            logger.info("Generating summary...")
            outputs = pipe(text, **gen_kwargs)[0]["summary_text"]
            
            # Clean up the output - remove unwanted characters and extra whitespace
            outputs = outputs.replace("<n>", " ").replace("\n", " ").strip()
            # Remove multiple spaces
            import re
            outputs = re.sub(r'\s+', ' ', outputs)
            
            logger.info("Summary generated successfully")
            return outputs
            
        except Exception as e:
            logger.error(f"Error in prediction: {str(e)}")
            raise e

        