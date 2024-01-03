from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--user-data-dir=/home/kirill/scrpts_test/tmp")

driver = webdriver.Chrome(options=chrome_options)

url = "https://dashboard.egamings.com/d/000000006/business%3a-operations?orgId=1&refresh=30s"
driver.get(url)

time.sleep(10)

try:
    login_input = driver.find_element(By.NAME,"user")
    password_input = driver.find_element(By.NAME,"password")

    login_input.send_keys("your_login")
    password_input.send_keys("your_password")

    password_input.send_keys(Keys.RETURN)
except NoSuchElementException:
    print('Not detected login and password')

time.sleep(5)  

actions = ActionChains(driver)
actions.send_keys(Keys.END)
actions.perform()

time.sleep(5)

driver.execute_script("window.open('','_blank');")
driver.switch_to.window(driver.window_handles[1])

new_url = "https://thewiki.egamings.com/pages/viewpage.action?pageId=1933349"
driver.get(new_url)

time.sleep(10)

continue_button = driver.find_element(By.XPATH,"//span[text()='Продолжить с именем пользователя и паролем']")
continue_button.click()

time.sleep(10)

try:
    login_input = driver.find_element(By.CLASS_NAME,"text")
    password_input = driver.find_element(By.CLASS_NAME,"password")

    login_input.send_keys("your_login")
    password_input.send_keys("your_password")

    password_input.send_keys(Keys.RETURN)
except NoSuchElementException:
    print('Not detected login and password')

time.sleep(10)

actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_DOWN * 10)
actions.perform()

time.sleep(20)


