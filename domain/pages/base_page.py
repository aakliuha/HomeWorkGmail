from playwright.sync_api import Page, Locator
from playwright.sync_api import TimeoutError


class BasePage:
    """This class contains the high-level methods common for all pages"""
    def __init__(self, page: Page):
        self.page: Page = page

    def navigate_to_url(self, url: str) -> None:
        self.page.goto(url)

    def get_element_by_locator(self, locator: str) -> Locator:
        element = self.page.locator(locator)
        return element

    def input_into_field(self, locator: str, value: str|int) -> None:
        try:
            element = self.get_element_by_locator(locator)
            element.fill(value)
        except TimeoutError:
            print(f"element with {locator} locator wasn't found")
            raise

    def click(self, locator: str) -> None:
        try:
            element = self.get_element_by_locator(locator)
            element.click()
        except TimeoutError:
            print(f"element with {locator} locator wasn't found")
            raise





