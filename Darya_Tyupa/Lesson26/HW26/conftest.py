import pytest
from selenium.webdriver import Firefox

from HW26.pages.main_page import MainPage


@pytest.fixture(scope='session')
def driver():
    driver = Firefox()
    yield driver
    driver.quit()
