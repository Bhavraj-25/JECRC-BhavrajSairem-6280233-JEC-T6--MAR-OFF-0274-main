from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = opts)

## 1
driver.get("https://the-internet.herokuapp.com/login")

## 2
uname = driver.find_element(By.CSS_SELECTOR, "input[name='username']")

## 3
passw = driver.find_element(By.CSS_SELECTOR, "input#password")

## 4
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

## 5
footer = driver.find_element(By.CSS_SELECTOR, "div#page-footer a")

print((uname, passw, login, footer))

sleep(2)
driver.quit()