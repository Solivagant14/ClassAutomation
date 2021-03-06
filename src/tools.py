#some handy functions needed in the project

from .driver import driver,wait10
from .data import USERNAME,PASSWORD
from os import name,system
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
import time
from math import ceil

def clear_screen():					#clears screen
    if name == 'nt':
        _ = system('cls')       # for windows
    else:
        _ = system('clear')     # for mac and linux

def scroll():
	height = driver.get_window_size()['height']
	main_content = driver.find_element_by_id("main-content-inner")
	scroll_height = driver.execute_script("return arguments[0].scrollHeight",main_content)
	for _ in range(ceil(scroll_height/height)):
		driver.execute_script(f"arguments[0].scrollBy(0,{height});",main_content) 
		time.sleep(1)

def logedin():
	try:						#opens the site if already logged in
		driver.get("https://learn.upes.ac.in/")
		wait10.until(ec.presence_of_element_located((By.XPATH, "//*[contains(@id,'course-list-course')]")))
	except:
		driver.maximize_window()
		time.sleep(2)
		logedin()
	scroll()

def login():						#opens the site and logs in 
	try:
		driver.get("https://learn.upes.ac.in/")
		button = driver.find_element_by_id("agree_button")
		button.click()
		driver.find_element_by_id("user_id").send_keys(USERNAME)
		driver.find_element_by_id("password").send_keys(PASSWORD)
		driver.find_element_by_id("entry-login").click()
	except:
		driver.maximize_window()
		time.sleep(2)
		login()

	try:
		wait10.until(ec.presence_of_element_located((By.XPATH, "//*[contains(@id,'course-list-course')]")))
	except:
		driver.maximize_window()
		time.sleep(2)
		logedin()
	scroll()

def find(xpath):
    element = driver.find_elements_by_xpath(xpath)
    if element:
        return element
    else:
        return False

def check_notice():                                                                                                #checks if their is any notice and quits it
	try:
		driver.implicitly_wait(2)
		time.sleep(2)
		notice = driver.find_element_by_xpath("//*[contains(@class,'notice')]")
		title = notice.find_element_by_class_name("title-container")
		button = title.find_element_by_tag_name("button")
		button.click()
	except NoSuchElementException:
		pass