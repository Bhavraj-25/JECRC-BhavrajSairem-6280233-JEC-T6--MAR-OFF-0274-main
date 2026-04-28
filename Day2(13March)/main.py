from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
# headless will make it work in the background
# opts.add_argument('--headless')
driver=webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(1)

'''
      find_element
Will return us the first occuring element
If not found - gives no such element found
'''
# name=driver.find_element(By.ID,'name')
# phone_no=driver.find_element(By.ID,'phone')
# nav_bar=driver.find_element(By.NAME,'Navbar')    #By name
# radio_button=driver.find_elements(By.CLASS_NAME,'form-cck-input')
# print(f'name is : {name}')
# print(phone_no)
# print(nav_bar)
# print(radio_button)   # return list
# print(len(radio_button))
# print('Element Found')
# driver.quit()
# Locators are used to find the attributes so that selenium can interact with it


# By css
# driver.find_element(By.CSS_SELECTOR,"#name")



# -------  CSS SELECTOR -------
# Simplest way to use css selector is by using .->class & #->id
# a[href*="testautomationpractice"] :- use this in search bar (ctrl+f) to locate long values that we need to find
# Works similar to regular expression
# ^ -> starts with ,$->ends with,*->all
# eg:- a[href$=".com"]
# animals=driver.find_elements(By.CSS_SELECTOR,'#animals')
# print(animals)

# Drawbacks of css selector:-
# We can only travel top-down not vice versa
# Difficulty in finding unique elements if want to search in the bar and use them
# for finding we use like :-
# we cant efficiently find our locators
# Cant find inner texts inner texts




''' ----------------------     XPath      ---------------------- '''
# Two types :- absolute  and  relative

# relative syntax:- //tag_name[@attribute_name='value']
xpath_phone=driver.find_elements(By.XPATH,"//input[@id='phone']")
print(xpath_phone)

xpath_form=driver.find_elements(By.XPATH,"//div[@class='form-group'][1]")
print(xpath_form)

xpath_datepicker=driver.find_element(By.XPATH,"//input[@id='datepicker']")
print(xpath_datepicker)

xpath_postHeader=driver.find_element(By.XPATH,"//div[@class='post-header']")
print(xpath_postHeader)

xpath_textbox=driver.find_element(By.XPATH,"//label[@for='textbox']")
print(xpath_textbox)


# Changing inner fields
email=driver.find_element(By.XPATH,"//label[text()='Email:']")
print(email)

datepicker3=driver.find_element(By.XPATH,"//label[text()='Date Picker 3: (Select a Date Range)']")
print(datepicker3)


brazil=driver.find_element(By.XPATH,"//option[contains(text(),'Brazil')]")   # contains will give us everything containing Brazil
print(brazil)

startwith_date=driver.find_element(By.XPATH,"//label[starts-with(text(),'Date')]")  # return all that starts with value
print(startwith_date)

