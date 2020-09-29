from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to
        # submit an empty item (ENTER on empty input box)
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # Home page refreshes, and an error message says that there cannot
        # be blank list items
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))

        # She tries again with some text for the item; now everything works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # She tries again to input a blank item
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # She receives a similar warning on the list page
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))

        # ...which she can correct by entering valid text
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea')
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
