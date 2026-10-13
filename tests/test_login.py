import allure
import pytest
from pages.login_page import LoginPage


@allure.feature("登录模块")
class TestLogin:

    @allure.story("正确账号登录")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.p0
    def test_login_success(self, driver):
        page = LoginPage(driver).open_login_page()
        page.login("standard_user", "secret_sauce")
        assert "inventory" in driver.current_url

    @allure.story("锁定用户登录")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.p0
    def test_login_locked_user(self, driver):
        page = LoginPage(driver).open_login_page()
        page.login("locked_out_user", "secret_sauce")
        assert "locked out" in page.get_error_message().lower()

    @allure.story("错误密码")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p0
    def test_login_wrong_password(self, driver):
        page = LoginPage(driver).open_login_page()
        page.login("standard_user", "wrong_password")
        assert "do not match" in page.get_error_message()

    @allure.story("空用户名")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.p1
    def test_login_empty_username(self, driver):
        page = LoginPage(driver).open_login_page()
        page.login("", "secret_sauce")
        assert "Username is required" in page.get_error_message()

    @allure.story("空密码")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.p1
    def test_login_empty_password(self, driver):
        page = LoginPage(driver).open_login_page()
        page.login("standard_user", "")
        assert "Password is required" in page.get_error_message()