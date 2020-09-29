from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to
        # submit an empty item (ENTER on empty input box)

        # Home page refreshes, and an error message says that there cannot
        # be blank list items

        # She inputs some text, which now is added to the list

        # She tries again to input a blank item

        # She receives a similar warning on the list page

        # ...which she can correct by entering valid text
        self.fail('write me')
