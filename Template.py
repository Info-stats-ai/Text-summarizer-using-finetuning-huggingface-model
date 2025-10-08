# Import required modules for file and directory operations
import os  # Operating system interface for file operations
import sys  # System-specific parameters and functions
from pathlib import Path  # Object-oriented filesystem paths
import logging  # Logging library for tracking events during execution

# Configure logging to display INFO level messages with timestamp, level, and message
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the project name to be used in the directory structure
project_name = "text-summarization"

# List of all files and directories to be created for the project structure
list_of_files = [
    ".github/workflows/.gitkeep",  # GitHub Actions workflow directory placeholder
    f"src/{project_name}/__init__.py",  # Main package initializer
    f"src/{project_name}/components/__init__.py",  # Components package for ML pipeline stages
    f"src/{project_name}/utils/__init__.py",  # Utilities package initializer
    f"src/{project_name}/utils/common.py",  # Common utility functions
    f"src/{project_name}/logging/__init__.py",  # Custom logging module
    f"src/{project_name}/config/__init__.py",  # Configuration package initializer
    f"src/{project_name}/config/configuration.py",  # Configuration management module
    f"src/{project_name}/pipeline/__init__.py",  # ML pipeline package initializer
    f"src/{project_name}/constants/__init__.py",  # Constants definition module
    f"src/{project_name}/entity/__init__.py",  # Entity classes for data structures
    "config/config.yaml",  # YAML configuration file for project settings
    "params.yaml",  # YAML file for model parameters and hyperparameters
    "app.py",  # Main application entry point (FastAPI/Flask app)
    "main.py",  # Main script to run the ML pipeline
    "Dockerfile",  # Docker container configuration for deployment
    "requirements.txt",  # Python package dependencies
    "setup.py",  # Python package setup and installation script
    "research/research.ipynb",  # Jupyter notebook for experimentation
    "README.md",  # Project documentation and instructions
    "LICENSE",  # Software license file
]

# Iterate through each file path in the list to create the project structure
for filepath in list_of_files:
    # Convert string path to Path object for better path handling
    filepath = Path(filepath)
    
    # Split the path into directory and filename components
    filedir, filename = os.path.split(filepath)
    
    # Check if there is a directory path (not just a filename)
    if filedir != "":
        # Create all intermediate directories if they don't exist (exist_ok=True prevents errors if directory exists)
        os.makedirs(filedir, exist_ok=True)
        # Log the directory creation
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    # Check if file doesn't exist OR if it exists but is empty (size = 0 bytes)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Open file in write mode and create empty file
        with open(filepath, "w") as f:
            pass  # Do nothing, just create empty file
            # Log the file creation
            logging.info(f"Creating empty file: {filepath}")
    else:
        # File already exists and has content, skip creation
        logging.info(f"File already exists: {filepath}")
