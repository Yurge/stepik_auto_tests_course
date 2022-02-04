from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

text = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
                                        )
button = browser.find_element(By.ID, "book").click()

x = browser.find_element(By.ID, "input_value").text
y = calc(x)

input = browser.find_element(By.ID, "answer").send_keys(y)
button2 = browser.find_element(By.ID, "solve").click()

alert = browser.switch_to.alert
print(alert.text)

browser.quit()