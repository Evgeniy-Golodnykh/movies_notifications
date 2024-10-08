import os

CINEMA_URL = 'https://kinomax.ru'
PREFIX = '/filmdata/'

DB_DRIVER_NAME = os.getenv('DB_DRIVER_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_USER = os.getenv('TELEGRAM_USER')

DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'
LOGFORMAT = '%(asctime)s [%(levelname)s] %(filename)s/%(funcName)s %(message)s'

START_TIME = '11:11'
SLEEP_DAYS = 1
BROWSER_PAUSE_DURATION = 10
