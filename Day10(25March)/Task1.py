from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://codepen.io/gdw96/pen/jOypoYL')
sleep(2)

iframe=driver.find_element(By.XPATH,"//iframe[@id='result']")
driver.switch_to.frame(iframe)

name_el=driver.find_element(By.ID,'username')
name_el.send_keys("abc")

pwd=driver.find_element(By.ID,'password')
pwd.send_keys("hello")
sleep(2)

eye_button=driver.find_element(By.ID,"showPsswd")
action=ActionChains(driver)
action.click_and_hold(eye_button).perform()
sleep(2)
action.release(eye_button).perform()

driver.find_element(By.CLASS_NAME,'submit').click()
sleep(5)

driver.refresh()
sleep(2)

driver.back()
sleep(5)