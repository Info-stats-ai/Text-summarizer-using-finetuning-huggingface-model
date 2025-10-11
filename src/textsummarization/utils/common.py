import os
from box.exceptions import BoxValueError
import yaml
from src.textsummarization import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations  # Validates that arguments match their type hints at runtime
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML configuration file and returns its contents as a ConfigBox
    
    ConfigBox allows dot notation access: config.model.name instead of config['model']['name']
    
    Args:
        path_to_yaml (Path): Filesystem path to the YAML file
                             Example: Path("config/config.yaml")
    
    Raises:
        ValueError: When the YAML file is empty (no content)
        Exception: When the file doesn't exist, can't be read, or has invalid YAML syntax
    
    Returns:
        ConfigBox: Dictionary-like object with dot notation access
    
    Example:
        >>> config = read_yaml(Path("config/config.yaml"))
        >>> print(config.model.learning_rate)
        0.0001
    """
    try:
        # Open the YAML file for reading
        # 'with' ensures the file is closed even if an exception occurs
        with open(path_to_yaml, "r") as yaml_file:
            
            # Parse YAML content into a Python dictionary
            # safe_load() prevents execution of arbitrary Python code (security)
            content = yaml.safe_load(yaml_file)
            
            # Log the successful file load (appears in logs/running_logs.log and console)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            
            # Wrap the dictionary in ConfigBox for dot notation access
            # ConfigBox({'a': {'b': 1}}) allows: box.a.b instead of box['a']['b']
            return ConfigBox(content)
    
    except BoxValueError:
        # yaml.safe_load() returns None when the file is empty
        # ConfigBox(None) raises BoxValueError
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        # Catch all other exceptions:
        # - FileNotFoundError: file doesn't exist
        # - PermissionError: no read permission
        # - yaml.YAMLError: invalid YAML syntax
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a list of directories
    
    Args:
        path_to_directories (list): List of directory paths to create
        verbose (bool): If True, logs directory creation. Default is True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")