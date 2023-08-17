import logging

from constants import (
    DATABASE_NAME, DATETIME_FORMAT, DB_HOST, DB_PORT, DRIVER_NAME,
    POSTGRES_PASSWORD, POSTGRES_USER,
)

POSTGRES_DB = {
    'drivername': DRIVER_NAME,
    'host': DB_HOST,
    'port': DB_PORT,
    'username': POSTGRES_USER,
    'password': POSTGRES_PASSWORD,
    'database': DATABASE_NAME,
}

LOGFORMAT = '%(asctime)s [%(levelname)s] %(filename)s/%(funcName)s %(message)s'


def configure_logging():
    logging.basicConfig(
        datefmt=DATETIME_FORMAT,
        format=LOGFORMAT,
        level=logging.INFO,
    )
