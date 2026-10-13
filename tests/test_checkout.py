import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("结算流程模块")
class TestCheckout:

    def _go_to_checkout(self, driver):
        """辅助方法：登录 → 加购 → 进入购物车 → 点击 Checkout"""
        LoginPage(driver).open_login_page().login("standard_user", "secret_sauce")
        inventory = InventoryPage(driver)
        inventory.add_first_item_to_cart()
        cart = inventory.go_to_cart()
        cart.wait_loaded()
        cart.checkout()
        return CheckoutPage(driver)

    @allure.story("完整结算流程")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.p0
    def test_checkout_success(self, driver):
        page = self._go_to_checkout(driver)
        page.fill_info("Zhang", "San", "123456")

        # 订单确认页应显示总金额
        total = page.get_summary_total()
        assert "Total:" in total, f"未显示总金额：{total}"

        # 完成下单
        page.finish_order()
        assert page.is_order_complete(), "未显示订单完成页"
        assert "Thank you for your order" in page.get_complete_header()

    @allure.story("结算信息必填校验")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p1
    def test_checkout_empty_first_name(self, driver):
        page = self._go_to_checkout(driver)
        page.fill_info("", "San", "123456")
        assert "First Name is required" in page.get_error_message()

    @allure.story("结算信息邮编必填校验")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.p2
    def test_checkout_empty_postal_code(self, driver):
        page = self._go_to_checkout(driver)
        page.fill_info("Zhang", "San", "")
        assert "Postal Code is required" in page.get_error_message()