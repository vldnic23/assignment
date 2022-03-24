import random

from selenium.webdriver.common.by import By

from _shared.utils.helpers import log
from aboutyou.pages.banners_popups.side_banner import AddToBasketContainer
from aboutyou.pages.generics.aboutyou_base_page import AboutYouBasePage


class ItemDetailsPage(AboutYouBasePage):

    # Buttons:
    _ADD_TO_BASKET_BUTTON = (
        By.XPATH,
        "//div[@data-testid='sectionEnd']//button[@data-testid='addToBasketButton']",
    )
    _ACTIVE_SIZES = (
        By.XPATH,
        "//div[contains(@data-testid, 'sizeOption') and contains(@data-testid, 'active')]",
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_basket = self.wait_for_element(self._ADD_TO_BASKET_BUTTON)

    def add_to_basket_with_random_size(self):
        """
        Method selects a random available size from the Size list
        and returns the AddToBasketContainer object.
        """

        self.add_to_basket.click()
        sizes = self.wait_for_elements(self._ACTIVE_SIZES)
        random_size = random.choice(sizes)
        random_size.click()
        log("Item added to basket.")

        return AddToBasketContainer(self.driver)
