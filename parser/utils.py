import time

from constants import CINEMA_URL, DEBUG, PAUSE_DURATION, SCREEN_RESOLUTION
from selenium import webdriver
from selenium.webdriver.common.by import By

CSS_DATES = 'div.calendar div button'
CSS_MOVIES = 'div.daily-seance-item__seance-title'
RESPONSE_ERROR_MESSAGE = 'An error {error} occurred when loading the page{url}'


def get_sessions_dates():
    try:
        browser = webdriver.Safari() if DEBUG else webdriver.Chrome()
        browser.set_window_size(*SCREEN_RESOLUTION)
        browser.get(CINEMA_URL)
        time.sleep(PAUSE_DURATION)
        dates = browser.find_elements(By.CSS_SELECTOR, CSS_DATES)
        result = ['?date=' + date.get_attribute('data-date') for date in dates]
        browser.quit()
        return result
    except Exception as error:
        raise ConnectionError(
            RESPONSE_ERROR_MESSAGE.format(url=CINEMA_URL, error=error)
        )


def get_movies(url):
    try:
        browser = webdriver.Safari() if DEBUG else webdriver.Chrome()
        browser.set_window_size(*SCREEN_RESOLUTION)
        browser.get(url)
        time.sleep(PAUSE_DURATION)
        movies = browser.find_elements(By.CSS_SELECTOR, CSS_MOVIES)
        result = [movie.text.strip() for movie in movies]
        browser.quit()
        return sorted(set(result))
    except Exception as error:
        raise ConnectionError(
            RESPONSE_ERROR_MESSAGE.format(url=url, error=error)
        )
