from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.maximize_window()

driver.get("https:/www.amazon.in")

wait = WebDriverWait(driver, 10)
search = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='twotabsearchtextbox']")))
search.send_keys("bambu labs a1")

suggest = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='left-pane-results-container']")))

four = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='left-pane-results-container']/descendant::*[22]")))
four.click()

sort = wait.until(EC.element_to_be_clickable((By.ID, "a-autoid-0-announce")))
sort.click()

new = wait.until(EC.element_to_be_clickable((By.ID, "s-result-sort-select_4")))
new.click()

free = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Free Shipping']/preceding-sibling::div//i")))
free.click()

detail_path = "//div[@class='a-section a-spacing-small puis-padding-left-small puis-padding-right-small']//div//a//h2//span[1]"
detail = wait.until(EC.presence_of_element_located((By.XPATH, detail_path)))
print(detail.text, "\n")

price_path = "//div[@class='a-section a-spacing-none a-spacing-top-small s-price-instructions-style']//div//div//a//span//span[2]//span[2]"
price = wait.until(EC.presence_of_element_located((By.XPATH, price_path)))
print("Price is: ", price.text)

sleep(1)
driver.quit()