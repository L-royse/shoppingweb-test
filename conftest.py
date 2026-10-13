import pytest
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """每个测试用例独享一个浏览器实例"""
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--start-maximized")
    # 如需走 Fiddler 抓包，取消下面这行注释
    # options.add_argument("--proxy-server=http://127.0.0.1:8866")

    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """用例失败时自动截图并附加到 Allure 报告"""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            path = f"reports/screenshots/{item.name}.png"
            driver.save_screenshot(path)
            allure.attach.file(
                path,
                name="失败截图",
                attachment_type=allure.attachment_type.PNG,
            )