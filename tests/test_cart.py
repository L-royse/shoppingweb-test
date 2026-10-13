import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@allure.feature("购物车模块")
class TestCart:

    def _login_and_go_inventory(self, driver):
        LoginPage(driver).open_login_page().login("standard_user", "secret_sauce")
        return InventoryPage(driver)

    @allure.story("添加单个商品到购物车")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.p0
    def test_add_single_item(self, driver):
        page = self._login_and_go_inventory(driver)
        page.add_first_item_to_cart()
        assert page.get_cart_badge_count() == 1, "购物车角标不是 1"

    @allure.story("添加多个商品到购物车")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.p0
    def test_add_multiple_items(self, driver):
        page = self._login_and_go_inventory(driver)
        page.add_items_to_cart(3)
        assert page.get_cart_badge_count() == 3, "购物车角标不是 3"

    @allure.story("购物车信息展示完整")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p1
    def test_cart_item_info(self, driver):
        page = self._login_and_go_inventory(driver)
        page.add_first_item_to_cart()
        cart = page.go_to_cart()

        assert cart.get_item_count() == 1, "购物车条目数不对"
        assert len(cart.get_item_names()) == 1, "商品名称缺失"
        assert len(cart.get_item_prices()) == 1, "商品价格缺失"
        assert cart.get_item_quantities()[0] == "1", "商品数量不是 1"

    @allure.story("移除购物车商品")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.p0
    def test_remove_item(self, driver):
        page = self._login_and_go_inventory(driver)
        page.add_items_to_cart(2)
        cart = page.go_to_cart()

        assert cart.get_item_count() == 2, "添加后数量不对"
        cart.remove_first_item()
        assert cart.get_item_count() == 1, "移除后数量不对"