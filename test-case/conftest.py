import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

DEFAULT_SCREEN_WIDTH = 1680
DEFAULT_SCREEN_HEIGHT = 1050
HEADLESS = os.getenv("HEADLESS", False)


@pytest.fixture
def setup(request):
    chrome_options = Options()
    window_size = (DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
    downloads_dir = "{}/Downloads".format(str(Path.home()))
    Path(downloads_dir).mkdir(parents=True, exist_ok=True)

    if bool(HEADLESS):
        chrome_options.headless = True
        window_size = (DEFAULT_SCREEN_WIDTH, 4320)

    chrome_options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": downloads_dir,
            "download.prompt_for_download": False,
        },
    )

    # install chromedriver
    capabilities = DesiredCapabilities.CHROME
    driver = webdriver.Chrome(
        ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(),
        options=chrome_options,
        desired_capabilities=capabilities,
    )
    driver.set_window_size(*window_size)

    driver.set_window_position(0, 0)

    driver.implicitly_wait(0)

    if request.cls:
        request.cls.driver = driver
        request.cls.downloads_dir = downloads_dir

    yield driver

    driver.quit()
