from src.textsummarization.logging import logger
from src.textsummarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textsummarization.components.data_ingestion import DataIngestion
from src.textsummarization.pipeline.stage_02_data_tranformation_pipeline import DataTransformationPipeline
from src.textsummarization.pipeline.stage_03_data_trainer_pipeline import ModelTrainerPipeline
from src.textsummarization.pipeline.stage_04_data_evaluation_pipeline import ModelEvaluationPipeline
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

#STAGE_NAME = "Model Trainer Stage"
#try:
    #logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    #obj = ModelTrainerPipeline()
    #obj.main()
#    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
#except Exception as e:
    #logger.exception(e)
    #raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e