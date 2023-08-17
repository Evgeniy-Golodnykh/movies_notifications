import logging

from constants import CINEMA_URL, PAUSE_DURATION
from selenium import webdriver
from selenium.webdriver.common.by import By

CSS_MOVIES_URL = '.releases-item '
CSS_MOVIES_NAME = 'div.releases-item-description__title'
ERROR_MESSAGE = 'An error {error} occurred when loading the page {url}'


def get_movies():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    try:
        browser = webdriver.Chrome(options=options)
        browser.set_page_load_timeout(PAUSE_DURATION)
        browser.implicitly_wait(PAUSE_DURATION)
        browser.get(CINEMA_URL)
        movies = browser.find_elements(By.CSS_SELECTOR, CSS_MOVIES_URL)
        logging.info(f'collected some items - {movies}')
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
