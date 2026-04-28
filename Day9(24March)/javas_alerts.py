'''
Types of javascript alert includes: simple alert, accept alert, prompt alert
'''

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
sleep(2)
driver.maximize_window()
action = ActionChains(driver)

## Finding & clicking the SIMPLE ALERT element
driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
sleep(2)

## For CONFIRMATION ALERT element
driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
sleep(2)
alert = driver.switch_to.alert
# alert.accept() ## to accept the alert
alert.dismiss() ## to cancel the alert
sleep(2)

## PROMPT ALERT element
'''
In PROMPT ALERT there are multiple cases:
1. no prompt with accept
2. no prompt with deny
3. prompt with accept
4. prompt with deny 
'''
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
sleep(2)
alert = driver.switch_to.alert
alert.send_keys('qwerty')
alert.dismiss()
sleep(2)

## Switching to alert using waits
wait = WebDriverWait(driver ,5)
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
alert = wait.until(EC.alert_is_present())
sleep(2)
alert.accept()
sleep(3)