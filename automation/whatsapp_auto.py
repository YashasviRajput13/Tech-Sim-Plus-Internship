from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
time.sleep(60) 

search_box = driver.find_element(
    'xpath', '//div[@contenteditable="true"][@data-tab="3"]'
)
search_box.click()
search_box.send_keys("Sure Gupta Oist")
search_box.send_keys(Keys.ENTER)

time.sleep(5)  

pyautogui.typewrite(
    "Happy Birthday! 🎉🎂 Wishing you a fantastic year ahead!",
    interval=0.05
)
pyautogui.press("enter")

time.sleep(3)
driver.quit()
