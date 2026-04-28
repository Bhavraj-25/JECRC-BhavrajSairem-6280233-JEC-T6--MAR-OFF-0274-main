import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
sleep(2)

parent_win = driver.current_window_handle

driver.find_element(By.XPATH, "//a[text()='Click Here']").click()
sleep(2)
all_win = driver.window_handles
print(len(all_win)) ## Length of the windows opened

driver.switch_to.window(all_win[-1])    ## Accessing the latest open window
# print(driver.find_element(By.CLASS_NAME, 'example').text)

assert 'New' in driver.find_element(By.CLASS_NAME, 'example').text
print('Done')

driver.switch_to.window(parent_win) ## Switching back to parent window

'''
Even if we use driver.close() which closes the old window, technically the control should switch to the next window.
But in selenium the control still stays in the parent window, even though it has been closed.
'''

driver.switch_to.new_window('tab') ## For new tab to open
driver.switch_to.new_window('window')   ## For new window to open