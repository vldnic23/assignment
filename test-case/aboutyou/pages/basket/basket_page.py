from selenium.webdriver.common.by import By

from aboutyou.pages.generics.aboutyou_base_page import AboutYouBasePage
from aboutyou.pages.items.basket_item import BasketItem


class BasketPage(AboutYouBasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_page_to_load_with_element(
            (By.XPATH, self._BASKET_ITEM_PARENT_PATH)
        )

    def get_basket_items(self):
        """Method return the items from the basket as BasketItem type"""

        return self.get_items(BasketItem, self._BASKET_ITEM_PARENT_PATH)
