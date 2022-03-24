from enum import Enum

from selenium.webdriver.common.by import By

from aboutyou.pages.generics.aboutyou_base_page import AboutYouBasePage


class DetailName(Enum):
    BRAND_NAME = "brandName"
    FINAL_PRICE = "finalPrice"


class ItemPage(AboutYouBasePage):
    def __init__(self, driver, index, parent_locator):
        super().__init__(driver)
        self.index = index
        self.parent_locator = parent_locator

    def _get_item_locator(self):
        """
        Method is used across all Item objects.
        Used for passing in the path for the parent locator of items.
        Returns the parent path with index.
        """
        return f"{self.parent_locator}[{self.index}]"
