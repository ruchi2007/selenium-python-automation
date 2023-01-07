import pytest

from pages.homePage import HomePage
from pages.loginPage import LoginPage

from util import usercredential


@pytest.mark.usefixtures('setup')
class TestLogin:
    def test_verify_user_should_login_successfully(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_username(usercredential.username)
        lp.enter_password(usercredential.password)
        lp.click_submit_btn()
        print("\n tc1..............>success")

    def test_verify_user_should_logout_successfully(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.click_logout_icon()
        print("\n tc2............>success")

    def test_login_verify_error_message_for_invalid_credential(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_username(usercredential.inv_username)
        lp.enter_password(usercredential.inv_password)
        lp.click_submit_btn()
        assert "Invalid credentials" in lp.error_text_message()
        print("\n tc3..............>success")
