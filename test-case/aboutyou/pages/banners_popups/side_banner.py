from selenium.webdriver.common.by import By

from _shared.utils.helpers import log
from aboutyou.pages.basket.basket_page import BasketPage
from aboutyou.pages.generics.aboutyou_base_page import AboutYouBasePage


class AddToBasketContainer(AboutYouBasePage):
    _PARENT_PATH = "//div[@data-test-id='AddToBasketFlyInContainer']"

    # Buttons:
    _CLOSE_CONTAINER = (By.XPATH, f"{_PARENT_PATH}//div[@data-test-id='Icon']")
    _CHECKOUT_BUTTON = (
        By.XPATH,
        f"{_PARENT_PATH}//button[@data-test-id='CheckoutButton']",
    )
    _BASKET_BUTTON = (By.XPATH, f"{_PARENT_PATH}//a[@data-test-id='LinkToUrl']")

    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_button = self.wait_for_element(self._CHECKOUT_BUTTON)
        self.basket_button = self.wait_for_element(self._BASKET_BUTTON)

    def close_banner(self):
        from aboutyou.pages.items.item_details_page import ItemDetailsPage

        self.wait_for_element(self._CLOSE_CONTAINER).click()
        self.wait_for_element_to_disappear((By.XPATH, self._PARENT_PATH))
        log("Add to basket container closed.")
        return ItemDetailsPage(self.driver)

    def navigate_to_basket(self):
        self.basket_button.click()
        return BasketPage(self.driver)
