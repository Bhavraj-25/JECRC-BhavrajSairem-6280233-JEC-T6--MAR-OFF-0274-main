from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Chrome()
driver.get('https://demoqa.com/browser-windows')
sleep(2)

driver.find_element(By.ID,'tabButton').click()
driver.find_element(By.ID,'windowButton').click()
driver.find_element(By.ID,'messageWindowButton').click()

parent_window=driver.current_window_handle
all_wds=driver.window_handles

## Part 1
driver.switch_to.window(all_wds[1])
assert 'page' in driver.find_element(By.XPATH,'//h1[@id="sampleHeading"]').text,'cant be found'
driver.switch_to.window(parent_window)

## Part 2
driver.switch_to.window(all_wds[2])
assert 'page' in driver.find_element(By.ID,'sampleHeading').text.lower(),'cant be found'
driver.switch_to.window(parent_window)

## Part 3
driver.switch_to.window(all_wds[3])
driver.switch_to.window(parent_window)

sleep(2)

driver.quit()