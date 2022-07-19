import pytest
from selenium.webdriver import Chrome, Firefox
import sys
sys.path.append("./")
from consts.DriversConsts import CHROME
  
@pytest.fixture(scope='session')
def config_browser(config = CHROME):
  return config

@pytest.fixture(scope='session')
def set_cookie(driver):
    # Now set the cookie. This one's valid for the entire domain
    cookie = {'name' : 'foo', 'value' : 'bar'}
    driver.add_cookie(cookie)

@pytest.fixture
def driver(config_browser, request):

    URL = "https://www.saucedemo.com/"
    # Initialize WebDriver

    if(hasattr(request, 'param')):
        URL = request.param

    if config_browser == CHROME:
        driver = Chrome()
    elif config_browser == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(5)
    # Return the driver object at the end of setup

    driver.get(URL)
    yield driver

    # For cleanup, quit the driver
    driver.quit()
    