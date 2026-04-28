from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = opts)

driver.get("https://www.thesouledstore.com/?utm_source=google&utm_medium=cpc&utm_campaign=TSS_Search_Branded_Core_Revamped_RM&utm_adgroup=Brand_Core_Mispel&utm_adname=Core&utm_term=soul%20store&utm_network=g&utm_matchtype=p&utm_device=c&gad_source=1&gad_campaignid=23068823035&gclid=CjwKCAjw1N7NBhAoEiwAcPchp_VgOodDTzhm4zyAVskE60Bvoi6vp_Vd7u6ayvAHWYVfeQJcOEmZqRoCoUIQAvD_BwE")
soul = driver.title
sleep(3)
driver.switch_to.new_window('tab')

driver.get("https://www.nike.in")
nike = driver.title
sleep(3)
driver.switch_to.new_window('tab')

driver.get("https://www.hindustantimes.com")
times = driver.title
sleep(3)
driver.switch_to.new_window('tab')

driver.get("https://www.python.org/")
python = driver.title

print((soul, nike, times, python))

sleep(3)
driver.quit()