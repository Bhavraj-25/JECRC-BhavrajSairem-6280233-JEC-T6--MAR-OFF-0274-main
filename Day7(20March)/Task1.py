from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = opts)
driver.get(r"C:\Users\BHAVRAJ SAIREM\Desktop\selenium_capg\DAY_WISE\Day7(20March)\playlist.html")

song_list = driver.find_element(By.ID, "songs")
select = Select(song_list)
list_songs = [i.text for i in select.options]
# print(list_songs)
for songs in list_songs:
    if 'girl' in songs.lower() or 'love' in songs.lower():
        select.select_by_visible_text(songs)
print("selected songs: ", [i.text for i in select.all_selected_options])
driver.find_element(By.XPATH, "//button[text()='Add to Playlist']").click()

sleep(3)
driver.quit()