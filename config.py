import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="application.log",  # Logs will be written to this file
    filemode="a"  # Append to the log file
)
