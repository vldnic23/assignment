import pytest

from _shared.utils.helpers import get_env_var, log
from aboutyou.pages.banners_popups.cookie_banner import CookieBanner
from aboutyou.pages.banners_popups.country_selector_pop_up import CountrySelectorPopUp
from aboutyou.pages.generics.header_page import HeaderPage


@pytest.fixture
def open_app(setup, request):
    driver = setup
    app_base_url = get_env_var("BASE_URL")
    driver.get(app_base_url)
    log(f"Browser opening at: {app_base_url}")

    CookieBanner(driver).accept_cookies()
    CountrySelectorPopUp(driver).navigate_on_current_country()
    header = HeaderPage(driver)

    if request.cls:
        request.cls.base_url = app_base_url
        request.cls.driver = driver
        request.cls.header = header

    return header
