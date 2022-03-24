from selenium.webdriver.common.by import By

from _shared.utils.helpers import log
from aboutyou.pages.generics.item_page import ItemPage, DetailName
from aboutyou.pages.items.item_details_page import ItemDetailsPage


class ContentItem(ItemPage):
    def __init__(self, driver, index):
        super().__init__(driver, index, parent_locator=self._CONTENT_ITEM_PARENT_PATH)
        self.item_name = self._get_item_details_for(DetailName.BRAND_NAME)
        self.item_price = self._get_item_details_for(DetailName.FINAL_PRICE)

    def open_item_details(self):
        """Method returns ItemDetailsPage object after the content object is clicked."""

        self.wait_for_element((By.XPATH, self._get_item_locator())).click()
        log("Opening item details page.")
        return ItemDetailsPage(self.driver)

    def _get_item_details_for(self, detail_name: DetailName):
        """
        Method returns the text from field.
        Arg:
            - details_name, DetailName type object mentioning which field needs to be returned
        """

        detail_locator = (
            By.XPATH,
            f"{self._get_item_locator()}//*[@data-testid='{detail_name.value}']",
        )
        return self.wait_for_element(detail_locator).text
