'''
using sleep() in selenium is not good practice (not recommended) because it interrupts the flow of code execution
sleep waits as per the time mentioned even if the element is found early
'''

## We use wait for this: (To solve synchronization issues of a web application i.e. python runs fasted than website loads)
'''
waits will move to next line if element is found early; only waits till max time allotted 

implicitly_wait: waits globally for all elements to appear; not flexible and does not care if the element is visible or not
                 if element not found, throws: NoSuchElementException
                 implicitly_wait()
                 No need to import any additional libraries

explicitly_wait: works on a specific element
                 if element not found, throws: TimeoutException
                 needs obj of WebDriverWait(); obj.until()
                 Need to import WebDriverWait and expected_conditions
                 
fluent_wait:     advanced explicit wait with more control i.e. we use poll_frequency in the explicit wait
                 
POLL_FREQUENCY:  takes in ms (milli-seconds)
                 checks the element every time after specified ms i.e. 200ms means it will keep checking after 200ms until element is found
                 keeps looking till element is found and/or max time is reached
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get("https:/www.amazon.in")

## implicit wait
driver.implicitly_wait(10)
driver.find_element(By.ID, "gw-card-layout")
print("element found")

## explicit wait
wait_time = WebDriverWait(driver, 5, poll_frequency=0.8) ## default poll is 500ms, takes in seconds
button = wait_time.until(EC.presence_of_element_located((By.ID, "nav-link-accountList"))) ## requires a tuple as an arg
button.click()
print("button clicked")

## loading element in abc.com site (explicit wait)
driver.switch_to.new_window('tab')
driver.get("https:/abc.com")
wait_time2 = WebDriverWait(driver, 5, poll_frequency=0.2) ## default poll is 500ms, takes in seconds
load = wait_time2.until(EC.presence_of_element_located((By.ID, "preloader-animated_svg__svg3")))
print("loader element found within 5 sec")
title = driver.find_element(By.XPATH, "//span[text()='ABC SHOWS, SPECIALS & MORE']")
assert "SHOWS" in title.text, "is not loading"
print("working just fine")

## checking of enabled button before and after usint wait
wait_time3 = WebDriverWait(driver, 6)
driver.switch_to.new_window('tab')
driver.get("https:/demoga.com/dynamic-properties")
enable_before = driver.find_element(By.ID, "enableAfter")
print(enable_before.is_enabled())
enable_button = wait_time3.until(EC.element_to_be_clickable((By.ID, "enableAfter")))

if enable_button.is_enabled():
    enable_button.click()
    print(enable_button.text)
visible = wait_time3.until(EC.visibility_of_element_located((By.ID, "visibleAfter")))
visible.click()

## abc.com sliding dots link printing
driver.switch_to.new_window("tab")
driver.get("https:/abc.com")
wait_time4 = WebDriverWait(driver, 10)
imgs = wait_time4.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='tile--hero__container']/descendant::picture/img")))
for img in imgs:
    print(img.get_attribute('src'))

## select.is_multiple() --> if the options are multiple select or single select (True/False)
## select.deselect_by_index(index)
## select.deselect_all() --> deselects all option
## first_selected_option --> not a method/function; returns the first selected option; returns none
## all_selected_options --> not a method/function; returns list of options selected

sleep(5)
driver.quit()