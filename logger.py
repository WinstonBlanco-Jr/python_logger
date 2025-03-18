import logging
import os

def custom_logger(module_name, level=logging.DEBUG):
    # Create a logger with the specified module name
    logger = logging.getLogger(module_name)
    logger.setLevel(level)

    # Set up the console handler first for fallback logging
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Define the log file path and ensure the directory exists
    log_file = f"./log_file/{module_name}.log"
    try:
        # Create the log directory if it doesn’t exist
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        # Set up the file handler
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except Exception as e:
        # Log an error to the console if file handler setup fails
        logger.error(f"Error setting up file handler: {e}")

    return logger
