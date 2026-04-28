from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
action = ActionChains(driver)
wait = WebDriverWait(driver, 5)

driver.get("https://www.myntra.com/")
sleep(3)
men = driver.find_element(By.XPATH, "//a[@data-group='men']")

action.move_to_element(men).perform()

wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-reactid='33']")))
casual = driver.find_element(By.XPATH, "//a[@data-reactid='33']")
casual.click()

sleep(2)
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='search-searchProductsContainer row-base']")))

sleep(2)
for i in range(5):
    action.send_keys(Keys.PAGE_DOWN).perform()
    sleep(1)

sleep(2)