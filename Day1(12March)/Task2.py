from selenium import webdriver
from time import sleep


l=[webdriver.Chrome(),webdriver.Firefox(),webdriver.Edge()]
for i in l:
    driver=i
    driver.get("https://www.google.com")
    sleep(2)
