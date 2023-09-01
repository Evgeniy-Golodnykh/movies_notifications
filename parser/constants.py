import os

CINEMA_URL = 'https://radygakino.ru/'

DB_DRIVER_NAME = os.getenv('DB_DRIVER_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_USER = os.getenv('TELEGRAM_USER')

DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'
PAUSE_DURATION = 5
SLEEP_DAYS = 1
