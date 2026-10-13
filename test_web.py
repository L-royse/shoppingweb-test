from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# 最大化窗口，避免元素因窗口太小而被判定不可见
driver.maximize_window()

driver.get("https://www.baidu.com")

# 等元素出现在 DOM
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "kw"))
)

# 取第一个 kw 元素，不管可见不可见
search_box = driver.find_elements(By.ID, "kw")[0]

# 全部用 JS 操作，绕过 Selenium 的可见性/可交互性检查
driver.execute_script("arguments[0].focus();", search_box)
driver.execute_script("arguments[0].value = 'python';", search_box)
driver.execute_script(
    "arguments[0].dispatchEvent(new Event('input', {bubbles:true}));",
    search_box
)
driver.execute_script("arguments[0].form.submit();", search_box)

print("当前 URL:", driver.current_url)
print("页面标题:", driver.title)

input("按回车退出...")
driver.quit()