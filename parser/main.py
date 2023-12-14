import asyncio
import logging
import time

import schedule
from configs import configure_logging
from constants import SLEEP_DAYS, START_TIME
from database import add_to_db
from telegram_message import send_message
from utils import get_movies

START_MESSAGE = 'Parser started!'
FINISHED_MESSAGE = 'Parser found {count} new movie(s).'
RESTART_MESSAGE = f'Parser will be restarted after {SLEEP_DAYS} day(s).'
ERROR_MESSAGE = 'Error when compile a module: {error}.'
MOVIE_MESSAGE = 'Вышел новый фильм «{name}». Вся информация по ссылке {url}'


def main():
    """Parse theater site, add Movie instance to database and send message."""

    configure_logging()
    logging.info(START_MESSAGE)
    try:
        movies = get_movies()
        count = 0
        for movie in movies:
            name, url = movie
            if add_to_db(name, url):
                count += 1
                asyncio.run(
                    send_message(MOVIE_MESSAGE.format(name=name, url=url))
                )
    except Exception as error:
        logging.error(ERROR_MESSAGE.format(error=error), exc_info=True)
    logging.info(FINISHED_MESSAGE.format(count=count))
    logging.info(RESTART_MESSAGE)


schedule.every(SLEEP_DAYS).day.at(START_TIME).do(main)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(SLEEP_DAYS)
