from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = opts)

## 1
driver.get("https://www.wikipedia.org/")

## 2
search = driver.find_element(By.ID, "searchInput")

## 3
eng = driver.find_element(By.XPATH, "//div[@class='langlist langlist-large hlist']//a[text()='English']")
eng_link = eng.get_attribute("href")
print(eng_link)

## 4
logo = driver.find_element(By.CSS_SELECTOR, "span.central-textlogo__image.sprite.svg-Wikipedia_wordmark")
print(logo)

## 5
lang = driver.find_elements(By.CSS_SELECTOR, "div.langlist.langlist-large.hlist li a")
print("Number of languages: ", len(lang))

## 6
driver.back()
sleep(1)

## 7
driver.forward()
sleep(1)

## 8
driver.refresh()

## 9
title_page = driver.title
print(title_page)
sleep(1)

## 10
driver.quit()