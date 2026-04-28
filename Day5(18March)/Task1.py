from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")

checkbox = driver.find_element(By.LINK_TEXT, "/checkboxes")
drop_down = driver.find_element(By.PARTIAL_LINK_TEXT, "/drag_and_drop")
count = driver.find_element(By.TAG_NAME, "li")
print(len(count))
driver.switch_to.new_window("tab")
driver.get("https://the-internet.herokuapp.com/tables")

driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='jdoe@hotmail.com']/following-sibling::td[2]")
driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='Bach']/following-sibling::td/a[text()='delete']")
driver.find_element(By.XPATH, "//table[2]")
child = driver.find_element(By.XPATH, "//table[2]//td[text()='$100.00']")
parent = child.find_element(By.XPATH, "..")