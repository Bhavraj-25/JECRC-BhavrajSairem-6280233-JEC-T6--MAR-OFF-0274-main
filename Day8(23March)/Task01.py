from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
action = ActionChains(driver)

driver.get("https://www.formula1.com/")
sleep(3)
pirelli = driver.find_element(By.XPATH, "//h2[text()='2026 HIGHLIGHTS']")

## Scrolls to specific element
action.scroll_to_element(pirelli).perform()
sleep(2)

## For loop run till 5
for i in range(0,5):
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(3)

sleep(2)