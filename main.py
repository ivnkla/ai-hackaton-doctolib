from chatv2 import *
from api import *

#récupérer l'API de scaleway, ne pas oublier de configurer votre propre .env !
API_KEY = get_api()

#signal pour le timeout
signal.signal(signal.SIGALRM, timeout_handler)

if __name__ == "__main__":
    get_report(API_KEY)