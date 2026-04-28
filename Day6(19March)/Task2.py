from time import sleep
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = opts)
driver.get("https://qavbox.github.io/demo/signup/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
uname = wait.until(EC.presence_of_element_located((By.ID, "username")))
uname.send_keys("First name")
# uname = driver.find_element(By.ID, "username")

mail = wait.until(EC.presence_of_element_located((By.ID, "email")))
mail.send_keys("fname@gmail.com")
# mail = driver.find_element(By.ID, "email")

phone = wait.until(EC.presence_of_element_located((By.ID, "tel")))
phone.send_keys("9080908070")
# phone = driver.find_element(By.ID, "tel")

try:
    wait_for_fax = WebDriverWait(driver, 2)
    fax = wait_for_fax.until(EC.element_to_be_clickable((By.ID, "fax")))
except TimeoutException:
    pass

upload = wait.until(EC.presence_of_element_located((By.NAME, "datafile")))
upload.send_keys(r"C:\Users\BHAVRAJ SAIREM\Downloads\0903.mp4")
# upload = driver.find_element(By.NAME, "datafile")

gender = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name='sgender']/option[2]")))
gender.click()
# gender = driver.find_element(By.ID, "sgender")

exp = driver.find_element(By.XPATH, "//div//label[text()='Years of Experience:']//following-sibling::input[2]")
exp.click()

skill = driver.find_element(By.XPATH, "//input[@id='ip'][2]")
skill.click()

tool = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='tools']/option[1]")))
tool.click()

button = wait.until(EC.presence_of_element_located((By.ID, "submit")))
button.click()

sleep(3)
driver.quit()



