from domain.pages.base_page import BasePage
from playwright.sync_api import Page, Locator
from domain.locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_field = LoginPageLocators.email_field
        self.password_field = LoginPageLocators.password_field
        self.email_next_button = LoginPageLocators.email_next_btn
        self.password_next_button = LoginPageLocators.password_next_btn
        self.greeting = LoginPageLocators.greeting
        self.wrong_email = LoginPageLocators.wrong_email_element
        self.wrong_password = LoginPageLocators.wrong_password_element
        self.empty_email = LoginPageLocators.empty_email_element
        self.empty_password = LoginPageLocators.empty_password_element
        self.inbox_main = LoginPageLocators.inbox_main_element

    def navigate_to_page(self, url: str) -> None:
        super().navigate_to_url(url)

    def enter_email(self, value: str) -> None:
        super().input_into_field(self.email_field, value)

    def enter_password(self, value: str) -> None:
        super().input_into_field(self.password_field, value)

    def click_email_next_btn(self) -> None:
        super().click(self.email_next_button)

    def click_password_next_btn(self) -> None:
        super().click(self.password_next_button)

    @property
    def get_main_element(self) -> Locator:
        main_element = super().get_element_by_locator(self.inbox_main)
        return main_element

    @property
    def get_incorrect_email_element(self) -> Locator:
        login_error = super().get_element_by_locator(self.wrong_email)
        return login_error

    @property
    def get_incorrect_password_element(self) -> Locator:
        login_error = super().get_element_by_locator(self.wrong_password)
        return login_error

    @property
    def get_empty_email_element(self) -> Locator:
        empty_email = super().get_element_by_locator(self.empty_email)
        return empty_email

    @property
    def get_empty_password_element(self) -> Locator:
        empty_password = super().get_element_by_locator(self.empty_password)
        return empty_password