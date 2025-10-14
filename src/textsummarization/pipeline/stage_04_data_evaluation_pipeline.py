from src.textsummarization.config.configuration import ConfigurationManager
from src.textsummarization.components.Model_evaluation import ModelEvaluation
from src.textsummarization.logging import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.evaluate()