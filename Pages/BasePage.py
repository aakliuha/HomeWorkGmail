from playwright.sync_api import Page
from playwright.sync_api import TimeoutError


class BasePage:
    """This class contains the high-level methods common for all pages"""
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_url(self, url):
        self.page.goto(url)

    def get_element_by_locator(self, locator):
        element = self.page.locator(locator)
        return element

    def input_into_field(self, locator, value):
        try:
            element = self.get_element_by_locator(locator)
            element.fill(value)
        except TimeoutError:
            print(f"element with {locator} locator wasn't found")
            raise

    def click(self, locator):
        try:
            element = self.get_element_by_locator(locator)
            element.click()
        except TimeoutError:
            print(f"element with {locator} locator wasn't found")
            raise





