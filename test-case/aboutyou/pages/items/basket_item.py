from selenium.webdriver.common.by import By

from aboutyou.pages.generics.item_page import ItemPage


class BasketItem(ItemPage):
    def __init__(self, driver, index):
        super().__init__(driver, index, parent_locator=self._BASKET_ITEM_PARENT_PATH)
        self.item_name = self.get_item_name()
        self.item_price = self.get_item_price()

    def get_item_name(self):
        """Method returns the item's name from the basket item list"""

        item_name_locator = (
            By.XPATH,
            f"{self._get_item_locator()}//div[contains(@class, 'brandName')]",
        )
        return self.wait_for_element(item_name_locator).text

    def get_item_price(self):
        """Method returns the item's price from the basket item list"""

        item_price_locator = (
            By.XPATH,
            f"{self._get_item_locator()}//*[@data-test-id='BasketItemPrice']",
        )
        return self.wait_for_element(item_price_locator).text
