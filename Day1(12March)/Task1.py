from selenium import webdriver
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.get("https://www.google.com")
driver.minimize_window()

driver.refresh()
driver.back()
driver.forward()
driver.close()
driver.quit()
