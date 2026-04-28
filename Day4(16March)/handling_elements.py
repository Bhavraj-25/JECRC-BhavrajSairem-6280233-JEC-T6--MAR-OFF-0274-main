## Day 3 - handling entry fields e.g. text box, check box, radio button, etc

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options = opts)
driver.get('https://testautomationpractice.blogspot.com')

## Sends the name key to the name field using ID
name_field = driver.find_element(By.ID, 'name')
name_field.send_keys('Azad')
# name_field.clear() ## clears the text field
sleep(1)

## Using XPATH to find email element and sending keys
email = driver.find_element(By.XPATH, "//input[@id='email']")
email.send_keys('email@gmail.com')
# email.clear() ## same as clearing email text field
sleep(1)

## Handling buttons
driver.find_element(By.XPATH, "//button[@type='submit']").click() ## submit button handling
driver.find_element(By.ID, 'male').click() ## Radio button handling
# monday_check = driver.find_element(By.XPATH, "//label[text()='Monday']/preceding-sibling::input").click() ## Check box button handling
# driver.find_element(By.XPATH, "//input[@id='male']")
sleep(1)

sleep(1)

driver.switch_to.new_window('tab')
driver.get('https://www.amazon.in')

sleep(1)

search_field = driver.find_element(By.ID, 'twotabsearchtextbox')
search_field.send_keys('dreampolymer pla')

search_button = driver.find_element(By.ID, 'nav-search-submit-button')
search_button.click() ## manual method to enter search button

search_field = driver.find_element(By.ID, 'twotabsearchtextbox')
search_field.clear()
search_field.send_keys('bambulabs p2s', Keys.ENTER) ## Automatically enters the search button

print(search_field.get_attribute('class')) ## giving error because the entire DOM structure changes

checked = True
if checked:
    driver.find_element(By.XPATH, "//input[@id='male']").click()
    sleep(1)
elif checked:
    driver.find_element(By.XPATH, "//input[@id='female']").click()
    sleep(1)
else:
    pass


## Checking boxes in loop and uncheck them in reverse order
done = True
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

for day in days:
    day_wise = driver.find_element(By.XPATH, f"//label[@for='{day}']")
    day_wise.click()
    print(day_wise.text)
    sleep(1)
for day in reversed(days):
    day_wise = driver.find_element(By.XPATH, f"//label[@for='{day}']")
    day_wise.click()
    sleep(1)


## nav to flipkart, search for a prod, get attr of the prod, click on search, click on box/boxes in filter section, get text of the filer
driver.get("https://www.flipkart.com")
search_field = driver.find_element(By.XPATH, "//input[@class='nw1UBF v1zwn25']")
search_field.clear()

sleep(1)

driver.find_element(By.XPATH, "//span[text()='✕']").click()
search_field.clear()
sleep(1)
search_field.send_keys('mobiles', Keys.ENTER)

parent = driver.find_element(By.XPATH, "//div[@class='Ye50_w']")
child = parent.find_elements(By.XPATH, "//div[@class='tx4xZf StZidb']")
# print(child.get_attribute('title'))
for c in child:
    print(c.get_attribute('title'))
sleep(3)
driver.quit()