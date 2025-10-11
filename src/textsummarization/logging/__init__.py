import os
import sys
import logging

# Define the logs directory and log file path
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create logs directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging with both file and console handlers
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Write to file
        logging.StreamHandler(sys.stdout)    # Print to console
    ]
)

# Create and export the logger instance
logger = logging.getLogger("textsummarizationLogger")