# pip install selenium

from selenium import webdriver
import time

# Start Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.linkedin.com/login")
time.sleep(3)

email = driver.find_element('ID', "username")
email.send_keys("ryashasvi77@gmail.com")

time.sleep(2)

password = driver.find_element('ID', "password")
password.send_keys("12334567")

time.sleep(2)

# Click login button
login_btn = driver.find_element('XPATH', "//button[@type='submit']")
login_btn.click()

time.sleep(1000)
