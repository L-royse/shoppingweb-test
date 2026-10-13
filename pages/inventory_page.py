from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.cart_page import CartPage

class InventoryPage(BasePage):
    """Sauce Demo 商品列表页"""

    URL = "https://www.saucedemo.com/inventory.html"

    # 元素定位符
    SORT_DROPDOWN = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    ADD_TO_CART_BTNS = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def is_loaded(self):
        """判断是否已进入商品列表页"""
        return self.is_visible(self.SORT_DROPDOWN)

    def get_product_names(self):
        """获取当前页所有商品名称"""
        return [el.text for el in self.driver.find_elements(*self.ITEM_NAMES)]

    def get_product_prices(self):
        """获取当前页所有商品价格（字符串形式，如 $29.99）"""
        return [el.text for el in self.driver.find_elements(*self.ITEM_PRICES)]

    def get_product_count(self):
        return len(self.driver.find_elements(*self.ITEM_NAMES))

    def sort_by(self, value):
        """
        按指定方式排序
        value 可选：
          'az'  -> Name (A to Z)
          'za'  -> Name (Z to A)
          'lohi'-> Price (low to high)
          'hilo'-> Price (high to low)
        """
        from selenium.webdriver.support.ui import Select
        select = Select(self.find(self.SORT_DROPDOWN))
        select.select_by_value(value)

    def add_first_item_to_cart(self):
        """添加第一个商品到购物车"""
        self.driver.find_elements(*self.ADD_TO_CART_BTNS)[0].click()

    def add_items_to_cart(self, count):
        """添加前 count 个商品到购物车（每次重新抓取，避免 React 重渲染导致元素失效）"""
        for _ in range(count):
            buttons = self.driver.find_elements(*self.ADD_TO_CART_BTNS)
            buttons[0].click()

    def get_cart_badge_count(self):
        """获取购物车角标数字，没有商品时返回 0"""
        if self.is_visible(self.CART_BADGE, timeout=2):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def go_to_cart(self):
        from selenium.webdriver.support import expected_conditions as EC
        self.click(self.CART_LINK)
        self.wait.until(EC.url_contains("cart.html"))
        return CartPage(self.driver)

    def logout(self):
        self.click(self.MENU_BTN)
        self.click(self.LOGOUT_LINK)