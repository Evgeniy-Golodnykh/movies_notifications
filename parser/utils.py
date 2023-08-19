import time

from constants import CINEMA_URL, PAUSE_DURATION
from selenium import webdriver
from selenium.webdriver.common.by import By

CSS_MOVIES_URL = 'a[class$="releases-item "]'
CSS_MOVIES_NAME = 'div.releases-item-description__title'
ERROR_MESSAGE = 'An error {error} occurred when loading the page {url}'


def get_movies():
    """Parse theater site."""

    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-extensions')
    options.add_argument('--window-size=1920,1080')

    try:
        browser = webdriver.Firefox(options=options)
        browser.get(CINEMA_URL)
        time.sleep(PAUSE_DURATION)
        movies = browser.find_elements(By.CSS_SELECTOR, CSS_MOVIES_URL)
        results = [
            (movie.find_element(By.CSS_SELECTOR, CSS_MOVIES_NAME).text.strip(),
             movie.get_attribute('href').split('?')[0])
            for movie in movies
        ]
        browser.quit()
        return results
    except Exception as error:
        raise ConnectionError(
            ERROR_MESSAGE.format(error=error, url=CINEMA_URL)
        )
