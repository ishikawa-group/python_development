import logging
import sys

def function_one():
    logger.debug("This is a debug message from function_one")

def function_two():
    logger.info("This is an info message from function_two")

if __name__ == "__main__":
    # Configure logging in the main script
    logging.basicConfig(
        level=logging.DEBUG,  # Set log level
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),  # Output to console
            logging.FileHandler("app.log", mode="w")  # Output to file
        ]
    )

    # Create a logger for this module
    logger = logging.getLogger(__name__)

    logger.info("Starting the application")
    function_one()
    function_two()
    logger.warning("Application is ending")
