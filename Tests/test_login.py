from Pages.LoginPage import LoginPage
from Tests.test_base import TestBase



class TestLogin(TestBase):

    def test_login_happy_path(self):
        login_page = LoginPage(self.page)
        login_page.navigate_to_login_page("https://www.gmail.com")

        login_page.enter_email("python911tasks@gmail.com")

        login_page.click_next_btn()

        login_page.enter_password("afey tham ntsy ydtz")
        login_page.click_next_btn()






