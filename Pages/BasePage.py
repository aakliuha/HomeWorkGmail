from playwright.sync_api import Page

class BasePage:
    """This class contains the high-level methods common for all pages"""
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_url(self, url):
        self.page.goto(url)
        return self

    def find_element_by_xpath(self, xpath):
        element = self.page.locator(xpath)
        return element

    def input_into_field(self, xpath, value):
        element = self.find_element_by_xpath(xpath)
        element.fill(value)
        return self

    def click(self, xpath):
        element = self.find_element_by_xpath(xpath)
        element.click()
        return self

    def get_text(self, element):
        text = element.innerText()
        return text




