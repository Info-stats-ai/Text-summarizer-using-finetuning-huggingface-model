from dataclasses import dataclass
from pathlib import Path

# input to data ingestion using .yaml file
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path
    unzip_dir: Path


@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: str

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: str
    num_train_epochs: int
    warmup_steps: int
    weight_decay: float
    logging_steps: int
    eval_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int