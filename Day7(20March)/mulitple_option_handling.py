from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

multi_drop = driver.find_element(By.ID, "colors")
select = Select(multi_drop)
if select.is_multiple:
    select.select_by_value('blue')
    select.select_by_index(3)
    select.select_by_visible_text('Red')

print('before deselecting: ', [i.text for i in select.all_selected_options])
sleep(3)
select.deselect_all()
print('after deselecting: ', [i.text for i in select.all_selected_options])

## Song multiple select

driver.switch_to.new_window('tab')
driver.get(r"C:\Users\BHAVRAJ SAIREM\Desktop\selenium_capg\DAY_WISE\Day7(20March)\playlist.html")

song_list = driver.find_element(By.ID, "songs")
select = Select(song_list)
if select.is_multiple:
    select.select_by_index(0) ## selects the <option> not <optgroup>
print("Songs selected: ", [i.text for i in select.all_selected_options])
driver.find_element(By.XPATH, "//button[text()='Add to Playlist']").click()
# print("options include: ", select.options)

## Task 1: Select songs with 'girl' and 'love' in it
list_songs = [i.text for i in select.options]
# print(list_songs)
for songs in list_songs:
    if 'girl' in songs.lower() or 'love' in songs.lower():
        select.select_by_visible_text(songs)
print("selected songs: ", [i.text for i in select.all_selected_options])
driver.find_element(By.XPATH, "//button[text()='Add to Playlist']").click()

sleep(3)
driver.quit()