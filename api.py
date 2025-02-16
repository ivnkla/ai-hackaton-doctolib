from dotenv import load_dotenv
import os

#importation de l'API
def get_api():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    return api_key