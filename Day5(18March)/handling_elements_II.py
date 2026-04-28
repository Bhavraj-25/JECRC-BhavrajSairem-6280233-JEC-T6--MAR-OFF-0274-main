from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
# driver.get('https://testautomationpractice.blogspot.com')
#
# male = driver.find_element(By.XPATH, "//input[@id='male']")
# male.click()
# sleep(1)
#
# female = driver.find_element(By.XPATH, "//input[@id='female']")
# female.click()
# sleep(1)
#
# ## checking the day
# day_wise = driver.find_element(By.ID, "sunday")
# day_wise.click()
# sleep(1)

# print(male.is_displayed()) ## verifies the visibility of the element in the website
# print(female.is_enabled()) ## True if the button is enabled; can be used in text fields as well
# print(day_wise.is_selected()) ## For check boxes, drop down lists; True if selected

# ## opening lenskart tab
# driver.switch_to.new_window('tab')
# driver.get('https://www.lenskart.com/')
# driver.maximize_window()
#
# search = driver.find_element(By.ID, "autocomplete-0-input")
# sleep(2)
# search.send_keys("aviator glasses", Keys.ENTER)
# sleep(2)
#
# # lens = driver.find_element(By.ID, "lrd1")
# # lens.click()
#
# drop = driver.find_element(By.ID, "sortByDropdown")
# select = Select(drop)
# select.select_by_value('created')
#
# sleep(2)
#
# first_one = driver.find_element(By.XPATH, "//div[@class='sc-bf32d8a7-0 gOVKHN']/descendant::*[1]")
# first_one.click()

# assert 'GLASSES' in lens.text, 'did not find' ## True if element/text is present, to find element(s)
# print('found it')

## Handling drop down menus/lists               we use maximize so that elements don't overlap
# drop_down = driver.find_element(By.XPATH, "//select[@id='country']")
# select = Select(drop_down)
# select.select_by_visible_text("India")
# sleep(2)
# select.select_by_index(4)
# sleep(2)
# select.select_by_value('japan')
# sleep(1)

## Uploading file

sleep(3)
## uploading file
driver.switch_to.new_window('tab')
driver.get('https://the-internet.herokuapp.com/upload')
file = driver.find_element(By.ID, 'file-upload')
file.send_keys(r"C:\Users\BHAVRAJ SAIREM\Downloads\0903.mp4")
sleep(2)
upload = driver.find_element(By.ID, 'file-submit').click()
## downloading file
driver.get('https://the-internet.herokuapp.com/download')
driver.maximize_window()
driver.find_element(By.XPATH,'//a[text()="Screenshot 2025-12-24 164603.png"]').click()
sleep(10)
print('downloaded')


sleep(6)
driver.quit()
