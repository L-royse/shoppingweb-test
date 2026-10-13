from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Sauce Demo 购物车页"""

    URL = "https://www.saucedemo.com/cart.html"

    # 元素定位符
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    ITEM_QUANTITIES = (By.CSS_SELECTOR, ".cart_quantity")
    REMOVE_BTNS = (By.CSS_SELECTOR, "button[data-test^='remove']")
    CHECKOUT_BTN = (By.ID, "checkout")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")

    def wait_loaded(self):
        """等待购物车页面加载完成（以 Checkout 按钮出现为准）"""
        self.wait.until(
            lambda d: d.find_element(*self.CHECKOUT_BTN).is_displayed()
        )
        return self

    def get_item_count(self):
        """购物车中商品条目数"""
        self.wait_loaded()
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_item_count(self):
        """购物车中商品条目数"""
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_item_names(self):
        return [el.text for el in self.driver.find_elements(*self.ITEM_NAMES)]

    def get_item_prices(self):
        return [el.text for el in self.driver.find_elements(*self.ITEM_PRICES)]

    def get_item_quantities(self):
        return [el.text for el in self.driver.find_elements(*self.ITEM_QUANTITIES)]

    def remove_first_item(self):
        self.driver.find_elements(*self.REMOVE_BTNS)[0].click()

    def checkout(self):
        self.click(self.CHECKOUT_BTN)