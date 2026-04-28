from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = opts)
driver.get(r"C:\Users\BHAVRAJ SAIREM\Desktop\selenium_capg\DAY_WISE\Day7(20March)\playlist.html")

fav_band = 'Linkin Park'
song_list = driver.find_element(By.XPATH, f"//select[@id='songs']")
select = Select(song_list)

find_band = driver.find_element(By.XPATH, f"//select[@id='songs']//optgroup[@label='{fav_band}']")
listed_songs=find_band.text.split("\n")

for songs in listed_songs:
    # print(songs)
    select.select_by_visible_text(songs)

print([i.text for i in select.all_selected_options])

sleep(2)
driver.quit()