import logging
import config  # Import to apply logging configuration
from ui.interface import start_chat_interface

if __name__ == "__main__":
    logging.info("Application started.")
    try:
        start_chat_interface()
    except Exception as e:
        logging.error("An error occurred: %s", e, exc_info=True)
    finally:
        logging.info("Application finished.")