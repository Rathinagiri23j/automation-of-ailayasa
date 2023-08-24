import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching firefox browser")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching edge browser")
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########## Pytest html report ##############
def pytest_configure(config):
    config.option.metadata = {
        'Project name': 'Ailaysa',
        'Module': 'Log In',
        'Executed by': 'Rathinagiri'
    }


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


