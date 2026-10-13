import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.feature("商品列表模块")
class TestInventory:

    def _login_and_go(self, driver):
        """辅助方法：登录后进入商品列表页"""
        LoginPage(driver).open_login_page().login("standard_user", "secret_sauce")
        return InventoryPage(driver)

    @allure.story("商品默认展示")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.p0
    def test_products_displayed(self, driver):
        page = self._login_and_go(driver)
        assert page.is_loaded(), "未进入商品列表页"
        assert page.get_product_count() == 6, "商品数量不是 6"

    @allure.story("按名称 A→Z 排序")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p1
    def test_sort_name_asc(self, driver):
        page = self._login_and_go(driver)
        page.sort_by("az")
        names = page.get_product_names()
        assert names == sorted(names), f"名称未升序：{names}"

    @allure.story("按名称 Z→A 排序")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p1
    def test_sort_name_desc(self, driver):
        page = self._login_and_go(driver)
        page.sort_by("za")
        names = page.get_product_names()
        assert names == sorted(names, reverse=True), f"名称未降序：{names}"

    @allure.story("按价格从低到高排序")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p1
    def test_sort_price_asc(self, driver):
        page = self._login_and_go(driver)
        page.sort_by("lohi")
        prices = [float(p.replace("$", "")) for p in page.get_product_prices()]
        assert prices == sorted(prices), f"价格未升序：{prices}"