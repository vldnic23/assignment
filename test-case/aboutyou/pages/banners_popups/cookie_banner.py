from selenium.webdriver.common.by import By

from _shared.pages.base_page import BasePage
from _shared.utils.helpers import log


class CookieBanner(BasePage):

    # Text:
    _BANNER_TITLE = (By.CSS_SELECTOR, "h3#onetrust-policy-title")
    _BANNER_INFO = (By.ID, "onetrust-policy-text")

    # Buttons
    _ACCEPT_COOKIE_BUTTON = (By.ID, "onetrust-accept-btn-handler")
    _SETTINGS_BUTTON = (By.ID, "onetrust-pc-btn-handler")

    def __init__(self, driver):
        super().__init__(driver)
        self.accept_cookie_button = self.wait_for_element(self._ACCEPT_COOKIE_BUTTON)
        self.setting_button = self.wait_for_element(self._SETTINGS_BUTTON)
        self.banner_title = self.wait_for_element(self._BANNER_TITLE)
        self.banner_info = self.wait_for_element(self._BANNER_INFO)

    def accept_cookies(self):
        self.accept_cookie_button.click()
        self.wait_for_element_to_disappear(self._BANNER_INFO)
        log("Cookies accepted.")
