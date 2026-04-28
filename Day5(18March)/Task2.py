from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

fname = driver.find_element(By.ID, "firstName") ## first name
fname.send_keys('jack')
lname = driver.find_element(By.ID, "lastName") ## last name
lname.send_keys('ryan')
mail = driver.find_element(By.ID, "userEmail") ## mail
mail.send_keys('jackryan@gmail.com')
gender_button = driver.find_element(By.ID, "gender-radio-1").click() ## gender button
unum = driver.find_element(By.ID, "userNumber") ## user number
unum.send_keys("9090807088")
subj = driver.find_element(By.ID, "subjectsInput") ## subjects
subj.send_keys("phy and python")
hobby = driver.find_element(By.ID, "hobbies-checkbox-1").click() ## hobbies/interest button

upload = driver.find_element(By.ID, "uploadPicture") #3 uploading picture
upload.send_keys(r"C:\Users\BHAVRAJ SAIREM\Downloads\Screenshot 2026-03-18 at 22-34-33 The Internet.png")

address = driver.find_element(By.ID, "currentAddress") ## current address field
address.send_keys("classified address. can't access location")

state = driver.find_element(By.ID, "react-select-3-input")  ## state drop down select
state.send_keys("NCR", Keys.ENTER)

city = driver.find_element(By.ID, "react-select-4-input") ## city drop down select
city.send_keys("Noida", Keys.ENTER)

submit_button = driver.find_element(By.ID, "submit").click()    ## submitting