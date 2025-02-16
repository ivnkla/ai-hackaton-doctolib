from dotenv import load_dotenv
from loguru import logger
import os

#importation de l'API
def get_api():  
    load_dotenv()
    logger.info(os.getenv("API_KEY"))
    return os.getenv("API_KEY")
