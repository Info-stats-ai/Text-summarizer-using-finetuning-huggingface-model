import os
import urllib.request as request
import zipfile as zip
from src.textsummarization.logging import logger
from src.textsummarization.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                str(self.config.source_URL),
                str(self.config.local_data_file)
            )
            logger.info(f"Downloaded file {filename} with the following headers: {headers}")
        else:
            logger.info(f"File already exists of size")
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zip.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            
