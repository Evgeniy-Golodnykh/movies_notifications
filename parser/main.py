import asyncio
import logging
import time

import schedule
from configs import configure_logging
from constants import SLEEP_DAYS, START_TIME
from database import add_to_db
from telegram_message import send_message
from utils import get_movies

PARSER_START_MESSAGE = 'Parser started!'
PARSER_FINISHED_MESSAGE = 'Parser found {count} new movie(s).'
PARSER_ERROR_MESSAGE = 'Error when compile a module: {error}.'
TELEGRAM_MOVIE_MESSAGE = 'Вышел новый фильм [«{name}».]({url})'


def main():
    """Parse theater site, add Movie instance to database and send message."""

    configure_logging()
    logging.info(PARSER_START_MESSAGE)
    try:
        movies = get_movies()
        count = 0
        for movie in movies:
            name, url = movie
            if add_to_db(name, url):
                count += 1
                asyncio.run(
                    send_message(
                        TELEGRAM_MOVIE_MESSAGE.format(name=name, url=url)
                    )
                )
    except Exception as error:
        logging.error(PARSER_ERROR_MESSAGE.format(error=error), exc_info=True)
    logging.info(PARSER_FINISHED_MESSAGE.format(count=count))


schedule.every(SLEEP_DAYS).day.at(START_TIME).do(main)

if __name__ == '__main__':
    main()

    while True:
        schedule.run_pending()
        time.sleep(SLEEP_DAYS)
