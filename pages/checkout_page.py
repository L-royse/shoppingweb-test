from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Sauce Demo 结算流程（信息填写 → 订单确认 → 完成）"""

    # 第一步：信息填写页
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    # 第二步：订单确认页
    FINISH_BTN = (By.ID, "finish")
    SUMMARY_TOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    # 第三步：完成页
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")
    BACK_HOME_BTN = (By.ID, "back-to-products")

    def fill_info(self, first_name, last_name, postal_code):
        """填写收货信息"""
        self.input_text(self.FIRST_NAME, first_name)
        self.input_text(self.LAST_NAME, last_name)
        self.input_text(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BTN)
        return self

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)

    def is_error_displayed(self):
        return self.is_visible(self.ERROR_MSG)

    def get_summary_total(self):
        """订单确认页的总金额，如 'Total: $32.39'"""
        return self.get_text(self.SUMMARY_TOTAL)

    def finish_order(self):
        """点击 Finish 完成下单"""
        self.click(self.FINISH_BTN)
        return self

    def get_complete_header(self):
        """完成页的标题，如 'Thank you for your order!'"""
        return self.get_text(self.COMPLETE_HEADER)

    def is_order_complete(self):
        return self.is_visible(self.COMPLETE_HEADER)

    def back_to_products(self):
        self.click(self.BACK_HOME_BTN)