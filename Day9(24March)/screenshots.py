import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

## gets the current working directory path
folder = os.path.join(os.getcwd(), "Screenshots")   ## gets curr working dir, name of folder: "Screenshots"
os.makedirs(folder, exist_ok = True)  ## path of folder, if it does not exist, create one

driver = webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
action = ActionChains(driver)

sleep(2)

'''
Two ways to take screenshot:
1. taking whole page
2. taking ss of particular element
'''
driver.save_screenshot(f'{folder}/full_page.png')    ## whole page screenshot
sleep(3)

ele = driver.find_element(By.XPATH, "(//div[@class='ADXRXN AsRsEE'])[3]/descendant::img")
action.scroll_to_element(ele).perform()
sleep(1)
ele.screenshot(f'{folder}/ele_ss.png')
sleep(2)