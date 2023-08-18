import logging

from constants import (
    DATETIME_FORMAT, DB_HOST, DB_PORT, DRIVER_NAME, POSTGRES_DB,
    POSTGRES_PASSWORD, POSTGRES_USER,
)

DATABASE = {
    'drivername': DRIVER_NAME,
    'host': DB_HOST,
    'port': DB_PORT,
    'username': POSTGRES_USER,
    'password': POSTGRES_PASSWORD,
    'database': POSTGRES_DB,
}

LOGFORMAT = '%(asctime)s [%(levelname)s] %(filename)s/%(funcName)s %(message)s'


def configure_logging():
    logging.basicConfig(
        datefmt=DATETIME_FORMAT,
        format=LOGFORMAT,
        level=logging.INFO,
    )
