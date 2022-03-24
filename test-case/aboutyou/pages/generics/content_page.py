from selenium.webdriver.common.by import By

from _shared.utils.helpers import log
from aboutyou.pages.filters.filter_section import FilterSection
from aboutyou.pages.generics.aboutyou_base_page import AboutYouBasePage
from aboutyou.pages.items.content_item import ContentItem


class ContentPage(AboutYouBasePage):

    _PRODUCTS_IMAGE = (By.XPATH, "//div[@data-testid='productImage']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_page_to_load_with_element(
            (By.XPATH, self._CONTENT_ITEM_PARENT_PATH)
        )

    def get_content_items(self):
        """Method returns the items from the basket as BasketItem type"""

        return self.get_items(ContentItem, self._CONTENT_ITEM_PARENT_PATH)

    def filter_items(self):
        """Method returns the FilterSection object in order to access the filter functionalities."""

        log("Preparing to filter the content.")
        return FilterSection(self.driver)
