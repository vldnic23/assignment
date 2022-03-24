from enum import Enum

from selenium.webdriver.common.by import By

from _shared.utils.helpers import log
from aboutyou.pages.generics.aboutyou_base_page import AboutYouBasePage


class SortType(Enum):
    TOPSELLER = "topseller"
    PRICE_HIGH = "price_high"
    PRICE_LOW = "price_low"
    NEW = "new"
    HIGHEST_REDUCTION = "highest_reduction"


class FilterSection(AboutYouBasePage):

    # Buttons:
    _SORT_BUTTON = (
        By.XPATH,
        "//section[contains(@data-testid, 'sortingOptionsDropdown')]",
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.sort_button = self.wait_for_element(self._SORT_BUTTON)

    def sort_by(self, sort_type: SortType):
        """Method sorts the content using a SortType object."""

        self.sort_button.click()
        sort_option_locator = (
            By.XPATH,
            f"//div[@data-testid='sortingOptionsDropdown-{sort_type.value}']",
        )
        self.wait_for_element(sort_option_locator).click()
        log(f"Content filtered by: {sort_type.value}")

        return self

    def apply_filters(self):
        """Method returns a new ContentPage object after filters are applied."""

        from aboutyou.pages.generics.content_page import ContentPage

        return ContentPage(self.driver)
