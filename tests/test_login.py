import allure
import pytest
from pages.login_page import LoginPage
from utils.yaml_until import load_login_cases


@allure.feature("登录模块")
class TestLogin:

    @allure.story("数据驱动登录测试")
    @pytest.mark.p0
    @pytest.mark.parametrize(
        "case",
        load_login_cases(),
        ids=lambda c: c["case_id"],   # 报告中显示用例ID
    )
    def test_login_data_driven(self, driver, case):
        """用 YAML 数据驱动登录测试"""
        allure.dynamic.title(f'{case["case_id"]} - {case["desc"]}')

        page = LoginPage(driver).open_login_page()
        page.login(case["username"], case["password"])

        if case["expected"] == "success":
            assert "inventory" in driver.current_url, "登录成功后未跳转商品列表页"
        else:
            actual = page.get_error_message()
            assert case["expected"] in actual, f"预期：{case['expected']}，实际：{actual}"