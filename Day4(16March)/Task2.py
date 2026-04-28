from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/radio-button")
sleep(4)

print(driver.title)

yes_button = driver.find_element(By.XPATH,"//label[@for='yesRadio']")
msg = yes_button.click()
print(yes_button.text)

radio_input = driver.find_element(By.ID,"yesRadio")
print(radio_input.get_attribute("class"))
print(radio_input.get_attribute('id'))

print(driver.current_url)

sleep(3)