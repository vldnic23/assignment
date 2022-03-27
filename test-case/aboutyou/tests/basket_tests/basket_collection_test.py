import allure
import pytest

from aboutyou.pages.filters.filter_section import SortType
from aboutyou.pages.generics.header_page import HeaderPage, Category, Gender


@allure.epic("Basket")
@allure.feature("Basket Clothing Collection")
class TestBasketCollections:
    @allure.story("Basket collection contains the properly selected items.")
    @pytest.mark.usefixtures("open_app")
    def test_basket_collection_contains_proper_items(self):
        # Return the content page after selecting category and gender
        content_page = (
            self.header.select_gender(Gender.MEN)
            .select_category(Category.SPORTSWEAR)
            .go_to_content()
        )

        # Filter items by highest price
        sportswear_filtered_items = (
            content_page.filter_items()
            .sort_by(SortType.PRICE_HIGH)
            .apply_filters()
            .get_content_items()
        )

        # Get the first 2 filtered items
        most_expensive_items = sportswear_filtered_items[:2]

        # Add each item in the basket
        for filtered_item in most_expensive_items:
            filtered_item.open_item_details().add_to_basket_with_random_size().close_banner()
            self.driver.back()

        # Navigate to basket and get all the previously added items
        basket_items = self.header.navigate_to_basket().get_basket_items()
        basket_items.reverse()
        
        # Assert that the items added in the basket
        # are the same as the filtered ones
        for index, basket_item in enumerate(basket_items):
            filtered_item = most_expensive_items[index]
            assert (
                basket_item.item_name == filtered_item.item_name
            ), "Names don't match."
            assert (
                basket_item.item_price == filtered_item.item_price
            ), "Prices don't match."
