from constants import BROWSER_PAUSE_DURATION, CINEMA_URL, PREFIX
from selenium import webdriver
from selenium.webdriver.common.by import By

CSS_MOVIES_URL = 'a[class$="Z4IP_eYWwdD_cOsOJsKJ SJ7_iJC5cQHgRsOlc3Z_"]'
CSS_MOVIES_NAME = 'h4.J7cZzMbW_T1JaXM9fHk9'
ERROR_MESSAGE = 'An error {error} occurred when loading the page {url}'
PATTERN = '(предсеанс. обсл)'


def get_movie_name_url(movie):
    name = movie.find_element(By.CSS_SELECTOR, CSS_MOVIES_NAME).text
    url = CINEMA_URL + PREFIX + movie.get_attribute('href').split('/')[-1]
    if PATTERN in name:
        name = name.split(PATTERN)[0]
    return name.strip(), url


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
        browser.implicitly_wait(BROWSER_PAUSE_DURATION)
        browser.get(CINEMA_URL)
        movies = browser.find_elements(By.CSS_SELECTOR, CSS_MOVIES_URL)
        browser.quit()
        return [get_movie_name_url(movie) for movie in movies if movie.text]
    except Exception as error:
        raise ConnectionError(
            ERROR_MESSAGE.format(error=error, url=CINEMA_URL)
        )
