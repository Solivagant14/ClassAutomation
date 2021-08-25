#some handy functions needed in the project

from .driver import driver,wait
from .data import USERNAME,PASSWORD,course_list
from os import name,system
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
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
	for i in range(ceil(scroll_height/height)):
		driver.execute_script(f"arguments[0].scrollBy(0,{height});",main_content) 
		time.sleep(1)

def login():						#opens the site and logs in 
	driver.get("https://learn.upes.ac.in/")

	button = driver.find_element_by_id("agree_button")
	button.click()

	driver.find_element_by_id("user_id").send_keys(USERNAME)
	driver.find_element_by_id("password").send_keys(PASSWORD)
	driver.find_element_by_id("entry-login").click()

	wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(@id,'course-list-course')]")))

	scroll()

def logedin():						#opens the site if already logged in
	driver.get("https://learn.upes.ac.in/")

	wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(@id,'course-list-course')]")))

	scroll()

def get_classes():					#extracts the available classes from the web page

	login()

	courses = driver.find_elements_by_xpath("//*[contains(@id,'course-link-')]")

	for course in courses:
		title = course.find_element_by_tag_name("h4")
		course_list[title.get_attribute('title')] = course.get_attribute('id')

	driver.minimize_window()

def find(xpath):
    element = driver.find_elements_by_xpath(xpath)
    if element:
        return element
    else:
        return False