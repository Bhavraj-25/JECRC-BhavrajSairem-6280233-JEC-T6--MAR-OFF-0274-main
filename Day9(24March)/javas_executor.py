import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
action = ActionChains(driver)

sleep(2)

'''
syntax for JS; document.body.scrollHeight because diff laptops have diff pixel size
basically detects the pix height and scrolls to the bottom
'''

## USING SCROLL TO
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(2)
## To the origin of the page
driver.execute_script('window.scrollTo(0,0);')

'''
SCROLL_TO will go to the exact points like (100,20) (0,0) but SCROLL_BY will go to reqd place from the current position so it is relative
That's why SCROLL_BY can take negative points but not SCROLL_TO
'''

## USING SCROLL BY
driver.execute_script('window.scrollBy(0,500);') ## scroll down by 500px
sleep(1)
driver.execute_script('window.scrollBy(0,-200);') ## scroll up by 200px
## SCROLLING TO ELEMENT
ele = driver.find_element(By.XPATH, "(//div[@class='ADXRXN AsRsEE'])[3]/descendant::img")
driver.execute_script('arguments[0].scrollIntoView();', ele)
sleep(2)
## CLICKING
click_ele = driver.find_element(By.XPATH, "(//div[text()='Join Pinterest'])[1]")
driver.execute_script('arguments[0].click()', click_ele)
sleep(2)