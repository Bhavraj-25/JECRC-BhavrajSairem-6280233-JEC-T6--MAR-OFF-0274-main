from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Chrome()
driver.get('https://demoqa.com/alerts')

## Part 1
alert_button=driver.find_element(By.ID,"alertButton")
alert_button.click()
sleep(2)
alert=driver.switch_to.alert
alert.accept()
sleep(2)

## Part 2
alert_button2=driver.find_element(By.ID,"timerAlertButton")
alert_button2.click()
sleep(6)
alert=driver.switch_to.alert
alert.accept()
sleep(2)

## Part 3
alert_button3=driver.find_element(By.ID,"confirmButton")
alert_button3.click()
sleep(2)
alert=driver.switch_to.alert
alert.accept()
assert 'ok' in driver.find_element(By.CLASS_NAME,"text-success").text.lower(),'have not accepted'
sleep(2)

## Part 4
alert_button4=driver.find_element(By.ID,"promtButton")
alert_button4.click()
alert=driver.switch_to.alert
alert.send_keys("hello")
alert.accept()

sleep(2)

driver.quit()