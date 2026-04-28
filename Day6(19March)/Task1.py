from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.maximize_window()

# driver.switch_to.new_window("tab")
driver.get("https:/abc.com")
wait_time4 = WebDriverWait(driver, 10)
imgs = wait_time4.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='tile--hero__container']/descendant::picture/img")))
for img in imgs:
    print(img.get_attribute('src'))

sleep(3)
driver.quit()