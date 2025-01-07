from dotenv import load_dotenv
from decouple import config

load_dotenv()

debug = config('DEBUG', default='False', cast=bool)