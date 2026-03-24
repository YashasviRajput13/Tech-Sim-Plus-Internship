from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Edge()
time.sleep(2)
driver.get("https://www.youtube.com/")

shorts_tab = driver.find_element('xpath','//*[@title="Shorts"]')
shorts_tab.click()

time.sleep(2)

search = driver.find_element('name','search_query')
search.send_keys("ichigo edit")
search.send_keys(Keys.ENTER)


time.sleep(5)
first_short = driver.find_element('xpath','//*[@id="contents"]/grid-shelf-view-model[2]/div[1]/div[1]/div[1]/ytm-shorts-lockup-view-model-v2/ytm-shorts-lockup-view-model/a/div')
first_short.click()


while True:
    while True:
        time.sleep(5)
        break
    next_btn = driver.find_element('xpath','//*[@id="navigation-button-down"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div[2]')
    next_btn.click()



time.sleep(1000)
driver.quit()