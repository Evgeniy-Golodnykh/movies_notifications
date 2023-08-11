import datetime as dt
import logging
import time

from configs import configure_logging
from constants import CINEMA_URL, DATETIME_FORMAT, SLEEP_DAY
from utils import get_movies, get_sessions_dates

START_MESSAGE = 'Parser started!'
PAUSE_MESSAGE = 'Parser will be restarted on {date_time}'
ERROR_MESSAGE = 'Error when compile a module: {error}'


def main():
    configure_logging()
    logging.info(START_MESSAGE)
    try:
        dates = get_sessions_dates()
        for date in dates[:1]:                              # delete
            print(*get_movies(CINEMA_URL + date), sep='\n')
    except Exception as error:
        logging.error(ERROR_MESSAGE.format(error=error))
    date_time = (dt.datetime.now() + dt.timedelta(days=3)).strftime(
        DATETIME_FORMAT
    )
    logging.info(PAUSE_MESSAGE.format(date_time=date_time))


if __name__ == '__main__':
    while True:
        main()
        time.sleep(SLEEP_DAY)
