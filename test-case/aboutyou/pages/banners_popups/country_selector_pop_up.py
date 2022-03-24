from selenium.webdriver.common.by import By

from _shared.pages.base_page import BasePage
from _shared.utils.helpers import log


class CountrySelectorPopUp(BasePage):
    # Buttons:
    _CONTINUE_ON_CURRENT_COUNTRY_BUTTON = (
        By.XPATH,
        "//button[@data-testid='countrySwitchCurrentCountry']",
    )
    _SWITCH_ON_RECOMMENDED_COUNTRY_BUTTON = (
        By.XPATH,
        "//a[@data-testid='countrySwitchTargetCountry']",
    )
    _X_CLOSE_POP_UP_BUTTON = (By.XPATH, "//*[@data-testid='modalDialogCloseIcon']")

    def __init__(self, driver):
        super().__init__(driver)
        self.continue_on_current_country = self.wait_for_element(
            self._CONTINUE_ON_CURRENT_COUNTRY_BUTTON
        )
        self.switch_to_recommended_country = self.wait_for_element(
            self._SWITCH_ON_RECOMMENDED_COUNTRY_BUTTON
        )
        self.close_pop_up = self.wait_for_element(self._X_CLOSE_POP_UP_BUTTON)

    def navigate_on_current_country(self):
        current_country_message = self.continue_on_current_country.text
        self.continue_on_current_country.click()
        self.wait_for_element_to_disappear(self._CONTINUE_ON_CURRENT_COUNTRY_BUTTON)
        log(f"Current country selected with message: {current_country_message}")
