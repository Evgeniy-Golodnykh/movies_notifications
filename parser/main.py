import asyncio
import datetime as dt
import logging
import time

from configs import configure_logging
from constants import DATETIME_FORMAT, SLEEP_DAYS
from database import add_to_db
from telegram_message import send_message
from utils import get_movies

START_MESSAGE = 'Parser started!'
PAUSE_MESSAGE = 'Parser will be restarted on {date_time}'
ERROR_MESSAGE = 'Error when compile a module: {error}'
USER_MESSAGE = 'Вышел новый фильм "{film}". Вся информация по ссылке {url}'


def main():
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
        logging.error(ERROR_MESSAGE.format(error=error))
    date_time = (
        dt.datetime.now() + dt.timedelta(days=SLEEP_DAYS)
    ).strftime(DATETIME_FORMAT)
    logging.info(PAUSE_MESSAGE.format(date_time=date_time))


if __name__ == '__main__':
    while True:
        main()
        time.sleep(SLEEP_DAYS * 24 * 60 * 60)
