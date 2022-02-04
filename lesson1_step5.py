from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer").send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, "[value='robots']").click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла