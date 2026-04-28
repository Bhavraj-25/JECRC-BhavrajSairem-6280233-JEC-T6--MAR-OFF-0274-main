# XPATH accessing
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)         # doesnt make the prgm wait
# just makes the tab remain open even when the prgm ends
# sleep() -> delays the prgm
driver=webdriver.Chrome(options=opts)

# driver.get("https://www.linkedin.com")
# sleep(2)
# driver.get("https://www.google.com")
# sleep(2)
# driver.get("https://www.youtube.com")
# sleep(2)

driver.get("https://www.amazon.com")
sleep(3)


# Accessing Ancestor
# // input[ @ id = 'email'] / ancestor::div

xpath_all=driver.find_element(By.XPATH,'//span[text()="All"]/ancestor::div[@id="nav-main"]')
print(xpath_all)

# Accessing Descendant
xpath_des_all=driver.find_element(By.XPATH,'//div[@id="nav-main"]/descendant::span[text()="All"]')
print(xpath_des_all)

xpath_des_all_upper_one=driver.find_element(By.XPATH,'//div[@class="nav-fill"]/descendant::span[text()="All"]')
print(xpath_des_all_upper_one)

# From parent to child
xpath_child_all=driver.find_element(By.XPATH,'//div[@class="nav-search-facade"]/child::span[text()="All"]')
print(xpath_child_all)


# Accessing preceding and following siblings
'''
eg:-
<div>class="g"
    <div>class="g1"
    <div>class="g2"
    <div>class="g3"
'''
# //div[@class="g2"]/preceding-sibling::div -> returns g1
# //div[@class="g2"]/following-sibling::div -> returns g3


xpath_anc_sib=driver.find_element(By.XPATH,'//a[text()="Fresh"]/ancestor::li/following-sibling::li[1] ')
print(xpath_anc_sib)
