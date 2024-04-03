from Pages.BasePage import BasePage
from Pages.locators.LoginPageLocators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_field = LoginPageLocators.email_field
        self.password_field = LoginPageLocators.password_field
        self.next_button = LoginPageLocators.next_btn

    def navigate_to_login_page(self, url):
        super().navigate_to_url(url)
        return self

    def click_sign_in_btn(self, element):
        super().click(element)
        return self

    def enter_email(self, value):
        super().input_into_field(self.email_field, value)
        return self

    def enter_password(self, value):
        super().input_into_field(self.password_field, value)
        return self

    def click_next_btn(self):
        super().click(self.next_button)
        return self

    def get_greeting(self, element):
        text = super().get_text(element)
        return text

    def find_element_email_field(self):
        element = super().find_element_by_xpath(self.email_field)
        return element

