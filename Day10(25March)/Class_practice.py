from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get('https://www.amazon.com/')
driver.maximize_window()
sleep(2)

assert 'Amazon' in driver.title,'cant find title'
assert 'amazon.com' in driver.current_url,'cant find the url'

driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Headphones",Keys.ENTER)
sleep(5)
driver.find_element(By.XPATH,"//span[text()='Sony']/preceding-sibling::div/descendant::i").click()
sleep(5)

action=ActionChains(driver)
prod=driver.find_element(By.XPATH,"(//span[contains(text(),'Sony')])[1]")
action.key_down(Keys.CONTROL).click(prod).key_up(Keys.CONTROL).perform()  # CTRl + click
all_windows=driver.window_handles

driver.switch_to.window(all_windows[-1])

assert 'sony' in driver.find_element(By.XPATH,"//span[@id='productTitle']").text.lower(),'not found'
sleep(2)

driver.find_element(By.XPATH,"//a[@id='add-to-cart-button']").click()
sleep(2)