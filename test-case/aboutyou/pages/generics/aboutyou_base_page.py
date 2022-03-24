from selenium.webdriver.common.by import By

from _shared.pages.base_page import BasePage
from _shared.utils.helpers import log


class AboutYouBasePage(BasePage):
    _CONTENT_ITEM_PARENT_PATH = (
        "//div[@style][1]//div[contains(@data-testid, 'productTileTracker')]"
    )
    _BASKET_ITEM_PARENT_PATH = "//li[contains(@data-test-id, 'BasketItem')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_page_to_load_with_element()

    def get_items(self, item_type, parent_path):
        """Method returns a list of items displayed in FE."""

        items = []
        amount_of_items = self.get_amount_of_items(parent_path)
        for index in range(1, amount_of_items + 1):
            item = item_type(self.driver, index)
            items.insert(index, item)

        log(f"Items: {items}")
        return items

    def get_amount_of_items(self, parent_path):
        """Method returns the length of a list of items displayed in FE."""

        items_locator = (By.XPATH, parent_path)
        return len(self.wait_for_elements(items_locator))
