from enum import Enum

from selenium.webdriver.common.by import By

from _shared.utils.helpers import log
from aboutyou.pages.basket.basket_page import BasketPage
from aboutyou.pages.generics.aboutyou_base_page import AboutYouBasePage
from aboutyou.pages.generics.content_page import ContentPage


class Category(Enum):
    OUTFITS = "Outfits"
    STORIES = "Stories"
    CLOTHING = "Clothing"
    SHOES = "Shoes"
    SPORTSWEAR = "Sportswear"
    ACCESSORIES = "Accessories"
    PREMIUM = "Premium"
    SALE = "SALE"
    BRANDS = "Brands"


class Gender(Enum):
    WOMEN = "Women"
    MEN = "Men"
    KIDS = "Kids"


class HeaderPage(AboutYouBasePage):
    # Buttons:
    _BASKET_BUTTON = (By.XPATH, "//li[@data-test-id='Basket']")
    _ABOUT_YOU_LOGO_BUTTON = (By.XPATH, "//div[@data-test-id='HeaderAboutYouLogo']")

    def __init__(self, driver):
        super().__init__(driver)
        self.about_you_logo = self.wait_for_element(self._ABOUT_YOU_LOGO_BUTTON)
        self.basket_button = self.wait_for_element(self._BASKET_BUTTON)

    def navigate_to_basket(self):
        """Method returns the BasketPage object after basket button is clicked."""

        log("Navigate to Basket.")
        self.basket_button.click()
        return BasketPage(self.driver)

    def select_category(self, category: Category):
        """Method selects a category from the header using the Category enum as param."""

        category_value = category.value
        category_locator = (
            By.XPATH,
            f"//li[@data-test-id='Header_navigation_list_item_{category_value}']",
        )
        self.wait_for_element(category_locator).click()
        log(f"{category_value} category selected.")

        return self

    def select_gender(self, gender: Gender):
        """Method selects a gender from the header using the Gender enum as param."""

        gender_value = gender.value
        gender_locator = (By.XPATH, f"//span[@data-test-id='Label_{gender_value}']")
        self.wait_for_element(gender_locator).click()
        log(f"{gender_value} gender selected.")

        return self

    def go_to_content(self):
        """Method return a new ContentPage object in order to access the content functionalities"""

        return ContentPage(self.driver)
