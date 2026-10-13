from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """所有页面对象的基类，封装通用操作"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)
        return self

    def find(self, locator):
        """等待元素出现在 DOM 中并返回"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        """等待元素可见并返回"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """等待元素可点击后点击"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        """清空并输入文本"""
        el = self.find_visible(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        """获取元素文本"""
        return self.find_visible(locator).text

    def is_visible(self, locator, timeout=5):
        """判断元素是否可见"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False