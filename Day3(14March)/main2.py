from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(3)
#
# # link text
# driver.find_element(By.LINK_TEXT,"Udemy Courses")
# print('fund link text')
#
# # partial link text
# driver.find_element(By.PARTIAL_LINK_TEXT,"Udemy")
# print('found partial ll')
#
#
# # Practice
#
# driver.find_element(By.XPATH,"//td[text()='Learn Java']/following-sibling::td[3]")
#
# print("found")
#

l=driver.find_elements(By.XPATH,"//td[text()='300']/preceding-sibling::td[3]")
for i in l:
    print(i.text)


new_l=driver.find_elements(By.XPATH,"//tbody[@id='rows']/descendant::tr/descendant::td[1]")
for i in new_l:
    print(i.text)