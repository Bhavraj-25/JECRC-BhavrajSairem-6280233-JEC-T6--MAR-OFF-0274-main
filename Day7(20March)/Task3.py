from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID, 'datepicker').send_keys('4/2/2026', Keys.ENTER)

driver.find_element(By.ID, "txtDate").click()
month = 'Dec'
date = '25'
year = '2003'
select = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
sel_year = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
select.select_by_visible_text(month)
sel_year.select_by_visible_text(year)

driver.find_element(By.XPATH, f"//a[text()='{date}']").click()


sleep(2)
driver.quit()