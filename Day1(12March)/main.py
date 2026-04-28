from selenium import webdriver
from time import sleep

# driver=webdriver.Chrome()
# sleep(2)


# driver=webdriver.Firefox()
# driver.maximize_window()                   # Make it full window
# sleep(2)
# driver.minimize_window()                   # Make it half screen
# driver.get("https://www.youtube.com")      # Access a site
# sleep(5)

# driver=webdriver.Edge()
# driver.maximize_window()
# driver.get("https://www.youtube.com")
# sleep(5)
# driver.get("https://www.youtube.com")
# driver.back()                     # Back Button
# sleep(2)
# driver.forward()                  # Forward Button
# sleep(2)
# driver.refresh()                  # refresh button
# sleep(2)
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Chrome()
# sleep(2)


# options=webdriver.ChromeOptions()
# options.binary_location=brave_Path
#
# driver=webdriver.Chrome(options=options)
# sleep(5)
#
# driver.maximize_window()                  # Make it full window
# driver.get(r"https://linkedin.com")       # Access a site
# sleep(2)
# driver.minimize_window()                  # Make it half screen
# sleep(2)


# driver=webdriver.Firefox()
# driver.maximize_window()
# driver.get("https://www.youtube.com")
# sleep(5)

# driver=webdriver.Edge()
# driver.maximize_window()
# driver.get("https://www.youtube.com")
# sleep(5)
# driver.get("https://www.youtube.com")
# driver.back()                     # Back Button
# sleep(2)
# driver.forward()                  # Forward Button
# sleep(2)
# driver.refresh()                  # refresh button
# sleep(2)

# opts=webdriver.ChromeOptions()
# # detach ,True will tell the brower to not automatically close the browser
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=opts)
#
# driver.get("https://www.youtube.com")
# driver.maximize_window()

# Similar for firefox but use set_preference
# opts=webdriver.FirefoxOptions()
# opts.set_preference("detach",True)
# driver=webdriver.Firefox(options=opts)
#
# driver.get("https://youtube.com")
# driver.close()
# driver.quit()
# driver.close() - Closes a single tab
# driver.quit() - Closes multiple tabs


opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.get("https://www.google.com")
print(driver.current_url)
print(driver.title)



