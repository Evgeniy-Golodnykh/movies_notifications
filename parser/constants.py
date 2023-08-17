import os

from dotenv import load_dotenv

load_dotenv()

CINEMA_URL = 'https://radygakino.ru/'

DRIVER_NAME = os.getenv('DRIVER_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DATABASE_NAME = os.getenv('DATABASE_NAME')

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_USER = os.getenv('TELEGRAM_USER')

DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'
PAUSE_DURATION = 7
SLEEP_DAYS = 2
