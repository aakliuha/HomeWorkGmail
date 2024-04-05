from domain.pages.login_page import LoginPage
from tests.test_base import TestBase
from playwright.sync_api import expect
from dotenv import dotenv_values

config = dotenv_values(".env")


class TestLogin(TestBase):

    def test_login_happy_path(self):
        login_page = LoginPage(self.page)
        login_page.navigate_to_login_page(config["MAIN_URL"])
        login_page.enter_email(config["VALID_EMAIL"])
        login_page.click_email_next_btn()
        login_page.enter_password(config["VALID_PASSWORD"])
        login_page.click_password_next_btn()
        expect(login_page.get_main_element).to_be_visible()

    def test_login_with_invalid_email(self):
        login_page = LoginPage(self.page)
        login_page.navigate_to_login_page(config["MAIN_URL"])
        login_page.enter_email("python475457developments@gmail.com")
        login_page.click_email_next_btn()
        expect(login_page.get_incorrect_email_element).to_have_text("Couldn’t find your Google Account")

    def test_login_with_invalid_password(self):
        login_page = LoginPage(self.page)
        login_page.navigate_to_login_page(config["MAIN_URL"])
        login_page.enter_email("python911tasks@gmail.com")
        login_page.click_email_next_btn()
        login_page.enter_password("wrong_pass!!!")
        login_page.click_password_next_btn()
        expect(login_page.get_incorrect_password_element).to_have_text("Wrong password. Try again or click Forgot "
                                                                       "password to reset it.")

    def test_login_with_empty_email(self):
        login_page = LoginPage(self.page)
        login_page.navigate_to_login_page(config["MAIN_URL"])
        login_page.click_email_next_btn()
        expect(login_page.get_empty_email_element).to_have_text("Enter an email or phone number")

    def test_login_with_empty_password(self):
        login_page = LoginPage(self.page)
        login_page.navigate_to_login_page(config["MAIN_URL"])
        login_page.enter_email("python911tasks@gmail.com")
        login_page.click_email_next_btn()
        login_page.click_password_next_btn()
        expect(login_page.get_empty_password_element).to_have_text("Enter a password")

    def test_login_with_email_in_wrong_format(self):
        login_page = LoginPage(self.page)
        login_page.navigate_to_login_page(config["MAIN_URL"])
        login_page.enter_email("python911tasks#gmail.com")
        login_page.click_email_next_btn()
        expect(login_page.get_incorrect_email_element).to_have_text("Couldn’t find your Google Account")

    def test_login_with_empty_spaces_password(self):
        login_page = LoginPage(self.page)
        login_page.navigate_to_login_page(config["MAIN_URL"])
        login_page.enter_email("python911tasks@gmail.com")
        login_page.click_email_next_btn()
        login_page.enter_password("        ")
        login_page.click_password_next_btn()
        expect(login_page.get_empty_password_element).to_have_text("Enter your password")



