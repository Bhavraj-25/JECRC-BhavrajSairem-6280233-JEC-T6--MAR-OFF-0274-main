from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
l=[webdriver.Chrome(),webdriver.Firefox(),webdriver.Edge()]
for i in l:
    driver=i
    driver.get("https://google.com")
    print(driver.title)
    print(driver.current_url)
