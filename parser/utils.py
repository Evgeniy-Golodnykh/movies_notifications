import time

from constants import CINEMA_URL, PAUSE_DURATION, SCREEN_RESOLUTION
from selenium import webdriver
from selenium.webdriver.common.by import By

CSS_MOVIES_URL = '.releases-item '
CSS_MOVIES_NAME = 'div.releases-item-description__title'
ERROR_MESSAGE = 'An error {error} occurred when loading the page {url}'


def get_movies():
    try:
        browser = webdriver.Chrome()
        browser.set_window_size(*SCREEN_RESOLUTION)
        browser.get(CINEMA_URL)
        time.sleep(PAUSE_DURATION)
        movies = browser.find_elements(By.CSS_SELECTOR, CSS_MOVIES_URL)
        return [
            (movie.find_element(By.CSS_SELECTOR, CSS_MOVIES_NAME).text.strip(),
             movie.get_attribute('href').split('?')[0])
            for movie in movies
        ]
    except Exception as error:
        raise ConnectionError(
            ERROR_MESSAGE.format(error=error, url=CINEMA_URL)
        )
    finally:
        browser.close()
        browser.quit()
