from src.textsummarization.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline
from src.textsummarization.logging import logger
from typing import Optional, Dict, Any
import re
import nltk

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(
        self,
        text: str,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        num_beams: Optional[int] = None,
        length_penalty: Optional[float] = None,
        num_sentences: Optional[int] = None,
    ) -> Dict[str, Any]:
        try:
            logger.info(f"Loading tokenizer from: {self.config.tokenizer_path}")
            tokenizer = AutoTokenizer.from_pretrained(str(self.config.tokenizer_path))

            logger.info(f"Loading model from: {self.config.model_path}")

            # Defaults based on input length if not provided by caller
            input_len_words = len(text.split())
            eff_max = (
                max_length if max_length is not None
                else 32 if input_len_words < 50
                else 64 if input_len_words < 200
                else 128
            )
            eff_min = min_length if min_length is not None else max(10, min(20, eff_max // 3))
            eff_num_beams = num_beams if num_beams is not None else 8
            eff_length_penalty = length_penalty if length_penalty is not None else 0.8

            gen_kwargs = {
                "min_length": eff_min,
                "max_length": eff_max,
                "num_beams": eff_num_beams,
                "length_penalty": eff_length_penalty,
            }

            pipe = pipeline("summarization", model=str(self.config.model_path), tokenizer=tokenizer)

            logger.info("Generating summary...")
            summary = pipe(text, **gen_kwargs)[0]["summary_text"]

            # Clean up the output - remove unwanted characters and extra whitespace
            summary = summary.replace("<n>", " ").replace("\n", " ").strip()
            summary = re.sub(r"\s+", " ", summary)

            # Optional: limit to first N sentences
            if num_sentences and num_sentences > 0:
                try:
                    nltk.data.find("tokenizers/punkt")
                except LookupError:
                    nltk.download("punkt", quiet=True)
                from nltk.tokenize import sent_tokenize
                sentences = sent_tokenize(summary)
                summary = " ".join(sentences[:num_sentences]).strip()

            logger.info("Summary generated successfully")
            return {
                "summary": summary,
                "input_length": input_len_words,
                "summary_length": len(summary.split()),
                "used_params": {
                    "min_length": eff_min,
                    "max_length": eff_max,
                    "num_beams": eff_num_beams,
                    "length_penalty": eff_length_penalty,
                    "num_sentences": num_sentences or 0,
                },
            }

        except Exception as e:
            logger.error(f"Error in prediction: {str(e)}")
            raise e

        