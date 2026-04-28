'''
Action chains include actions like keyboard press, mouse hover, mouse clicking actions, drag and drop, etc (mouse & keyboard actions)
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
driver.maximize_window()
sleep(3)

action = ActionChains(driver)
origin = driver.find_element(By.ID, "column-a")
target = driver.find_element(By.ID, "column-b")

## perform ensures that the action chosen is performed, otherwise it will not perform that action
action.drag_and_drop(origin, target).perform()
sleep(2)

driver.switch_to.new_window('tab')
driver.get("https://supertails.com/")

dogesh = driver.find_element(By.XPATH, "(//span[contains(text(), 'Dogs')])[1]")
action.move_to_element(dogesh).perform()
sleep(5)

driver.get("https://demoqa.com/droppable")
driver.maximize_window()
sleep(2)
drag_src = driver.find_element(By.ID, "draggable")
drag_tar = driver.find_element(By.ID, "droppable")

action.drag_and_drop(drag_src, drag_tar).perform()
sleep(2)
# assert 'Dropped' == drag_tar.text, "not dragged"
driver.find_element(By.ID, "droppableExample-tab-preventPropogation").click()
drag_box = driver.find_element(By.ID, "dragBox")
inner_drop = driver.find_element(By.ID, "notGreedyInnerDropBox")
action.drag_and_drop(drag_box, inner_drop).perform()

sleep(2)

driver.switch_to.new_window('tab')
driver.get("https://supertails.com/")
sleep(3)
catto = driver.find_element(By.XPATH, "//div[@data-ganame='Breed 5']")

## Scrolls to specific element
action.scroll_to_element(catto).perform()
sleep(2)

'''
SCROLL TO: (100,100); will scroll down to specified pixels (x,y)
SCROLL BY: (pixel_amt); scrolls down from the current position + the amount specified, eg: SCROLL BY(100): 0(current)+100(scroll by) = 100
Both support negative values specifying the cartesian numbers
'''

action.scroll_by_amount(0, -500).perform()
sleep(3)
action.scroll_from_origin(0, 0, 1000).perform()
sleep(5)

'''
action.click() is left click
action.context_click() is right click'
action.double_click() is double click (left
'''

## KEYBOARD ACTIONS ________________________________________________________________-

## Up by 100 pixels
action.send_keys(Keys.PAGE_UP).perform()
sleep(5)
## Down by 100 pixels
action.send_keys(Keys.PAGE_DOWN).perform()
sleep(5)
## Control key press (ctrl+A)
action.key_down(Keys.CONTROL).send_keys('a').perform() # press down and select ctrl+a
action.key_up(Keys.CONTROL).perform() # release the ctrl, a keys
sleep(2)

driver.get(r"C:\Users\BHAVRAJ SAIREM\Desktop\selenium_capg\DAY_WISE\Day8(23March)\new.html")
driver.maximize_window()
present = driver.find_element(By.ID, "presentAddress")
perm = driver.find_element(By.ID, "permanentAddress")
present.send_keys('JECRC, JAIPUR, RJ')
sleep(2)
present.click()
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
sleep(1)
action.key_down(Keys.CONTROL).send_keys('c').perform()  ## copy action
sleep(1)

perm.click()
action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform() ## paste action

driver.get(r"C:\Users\BHAVRAJ SAIREM\Desktop\selenium_capg\DAY_WISE\Day8(23March)\index1.html")
driver.maximize_window()
driver.find_element(By.ID, "password").send_keys('radar') ## sends password

sleep(3)

show_pd = driver.find_element(By.ID, "eyeBtn") ## Click on eye button to see the password
action.click_and_hold(show_pd).perform()
sleep(3)
action.release()