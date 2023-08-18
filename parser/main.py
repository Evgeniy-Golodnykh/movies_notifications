import asyncio
import logging
import time

from configs import configure_logging
from constants import SLEEP_DAYS
from database import add_to_db
from telegram_message import send_message
from utils import get_movies

START_MESSAGE = 'Parser started!'
PAUSE_MESSAGE = f'Parser will be restarted after {SLEEP_DAYS} days.'
ERROR_MESSAGE = 'Error when compile a module: {error}.'
USER_MESSAGE = 'Вышел новый фильм "{film}". Вся информация по ссылке {url}.'


def main():
    """Parse theater site, add Movie instance to database and send message."""

    configure_logging()
    logging.info(START_MESSAGE)
    try:
        movies = get_movies()
        for movie in movies:
            if add_to_db(movie):
                asyncio.run(send_message(
                    USER_MESSAGE.format(film=movie[0], url=movie[1])
                ))
    except Exception as error:
        logging.error(ERROR_MESSAGE.format(error=error), exc_info=True)
    logging.info(PAUSE_MESSAGE)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(SLEEP_DAYS * 24 * 60 * 60)
