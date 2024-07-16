import pytest
from selenium import webdriver

from Library.configure import Configuration


@pytest.fixture(params=["edge"])
def init_driver(request):
    browser = request.param

    if browser.lower() == "edge":
        driver = webdriver.Edge()

    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(Configuration.URL)
    yield driver
    driver.close()
