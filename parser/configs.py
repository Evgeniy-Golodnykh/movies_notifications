import logging

LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
LOG_DATE_FORMAT = '%d.%m.%Y %H:%M:%S'


def configure_logging():
    logging.basicConfig(
        datefmt=LOG_DATE_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
    )
