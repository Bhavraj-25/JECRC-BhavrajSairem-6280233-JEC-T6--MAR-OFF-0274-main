from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
sleep(3)

name = driver.find_element(By.XPATH,"//input[@name='username']")
name.clear()
name.send_keys("Admin")

password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys("admin123")

login = driver.find_element(By.XPATH,"//button[@type='submit']")
login.send_keys("admin123", Keys.ENTER)

url = driver.current_url
print('dashboard' in url)

print('successful login')
sleep(3)