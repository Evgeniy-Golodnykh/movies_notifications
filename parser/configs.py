import logging

from constants import DATETIME_FORMAT

DEBUG = True
LOGFORMAT = '%(asctime)s [%(levelname)s] %(filename)s/%(funcName)s %(message)s'


def configure_logging():
    logging.basicConfig(
        datefmt=DATETIME_FORMAT,
        format=LOGFORMAT,
        level=logging.INFO,
    )
