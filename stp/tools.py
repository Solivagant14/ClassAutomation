from .data import course_dict,login_dict
from .driver import driver,wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from os import name,system
from math import ceil
from time import sleep

def login():						#opens the site and logs in 
    driver.get("https://learn.upes.ac.in/")
    button = driver.find_element_by_id("agree_button")
    button.click()
    driver.find_element_by_id("user_id").send_keys(login_dict["username"])
    driver.find_element_by_id("password").send_keys(login_dict["password"])
    driver.find_element_by_id("entry-login").click()
    wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(@id,'course-list-course')]")))
    height = driver.get_window_size()['height']
    main_content = driver.find_element_by_id("main-content-inner")
    scroll_height = driver.execute_script("return arguments[0].scrollHeight",main_content)
    for _ in range(ceil(scroll_height/height)):
	    driver.execute_script(f"arguments[0].scrollBy(0,{height});",main_content) 
	    sleep(1)

def get_classes():					#extracts the available classes from the web page
    courses = driver.find_elements_by_xpath("//*[contains(@id,'course-link-')]")
    for course in courses:
        title = course.find_element_by_tag_name("h4")
        course_dict[title.get_attribute('title')] = course.get_attribute('id')
    driver.quit()

def clear_screen():					#clears screen
    if name == 'nt':
        _ = system('cls')       # for windows
    else:
        _ = system('clear')     # for mac and linux