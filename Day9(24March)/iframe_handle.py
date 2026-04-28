import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
sleep(2)
driver.maximize_window()
action = ActionChains(driver)

## Single iframe handling
# iframe = driver.find_element(By.ID, "singleframe")
# driver.switch_to.frame(iframe)
# sleep(2)
# driver.find_element(By.XPATH, "//input[@type = 'text']").send_keys('hello')
# sleep(2)

## Nested iframe handling
driver.find_element(By.XPATH, '//a[text()="Iframe with in an Iframe"]').click()
new_frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(new_frame)
nest_frame = driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(nest_frame)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys('hihihaha')
sleep(5)