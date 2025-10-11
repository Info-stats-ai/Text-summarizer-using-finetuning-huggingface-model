from src.textsummarization.logging import logger
from src.textsummarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textsummarization.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e