from Pages.BasePage import BasePage
from Pages.locators.LoginPageLocators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_field = LoginPageLocators.email_field
        self.password_field = LoginPageLocators.password_field
        self.next_button = LoginPageLocators.next_btn
        self.greeting = LoginPageLocators.greeting
        self.wrong_email = LoginPageLocators.wrong_email_element
        self.wrong_password = LoginPageLocators.wrong_password_element
        self.empty_email = LoginPageLocators.empty_email_element
        self.empty_password = LoginPageLocators.empty_password_element

    def navigate_to_login_page(self, url):
        super().navigate_to_url(url)

    def enter_email(self, value):
        super().input_into_field(self.email_field, value)

    def enter_password(self, value):
        super().input_into_field(self.password_field, value)

    def click_next_btn(self):
        super().click(self.next_button)

    @property
    def get_greeting_element(self):
        greeting = super().get_element_by_locator(self.greeting)
        return greeting

    @property
    def get_incorrect_email_element(self):
        login_error = super().get_element_by_locator(self.wrong_email)
        return login_error

    @property
    def get_incorrect_password_element(self):
        login_error = super().get_element_by_locator(self.wrong_password)
        return login_error

    @property
    def get_empty_email_element(self):
        empty_email = super().get_element_by_locator(self.empty_email)
        return empty_email

    @property
    def get_empty_password_element(self):
        empty_password = super().get_element_by_locator(self.empty_password)
        return empty_password