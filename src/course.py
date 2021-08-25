#this file has the class which is the blue print for all the classes

from .tools import logedin,timer
from .driver import driver,wait
from .data import CLASS_DURATION,LAB_DURATION,time_format
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
from datetime import datetime,timedelta
from selenium.common.exceptions import NoSuchWindowException,NoSuchElementException

class Course:
    def __init__(self,title,id):
        self.title = title      #title of the class
        self.id = id            #id of the WebElement

    def attend(self,first,start):
        driver.maximize_window()
        while True:
            try:
                driver.find_element_by_id(self.id).click()                                                          #clicks the course
                try:                                                                                                #checks if their is any notice and quits it
                    driver.implicitly_wait(5)
                    time.sleep(5)
                    notice = driver.find_element_by_xpath("//*[contains(@class,'notice')]")
                    title = notice.find_element_by_class_name("title-container")
                    button = title.find_element_by_tag_name("button")
                    button.click()
                except NoSuchElementException:
                    pass
                wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='sessions-list-dropdown']/span")))
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='sessions-list-dropdown']/span").click()
                driver.find_element_by_link_text("Course Room").click()                                             #clicks join session
                break
            except:
                logedin()
                
        blackboard_tab = driver.window_handles[0]           #naming the tabs
        session_tab = driver.window_handles[1]

        driver.switch_to_window(session_tab)                #switched to the session tab
        print("Attending ",self.title)

        if first:
            while True:                 #this deals with the video and audio check
                try:
                    wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='dialog-description-audio']/div[2]/button"))).click()
                    time.sleep(5)
                    wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='techcheck-video-ok-button']"))).click()
                    break
                except:
                    driver.refresh
            while True:                 #this deals with the tutorial announcement
                try:
                    wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='announcement-modal-page-wrap']/div/div[4]/button"))).click()
                    time.sleep(2)
                    break
                except:
                    driver.refresh()
            try:
                wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='tutorial-dialog-tutorials-menu-learn-about-tutorials-menu-close']"))).click()
            except:
                driver.refresh()

        end = (datetime.strptime(start,time_format) + timedelta(minutes=LAB_DURATION)).strftime(time_format) if 'Lab' in self.title else (datetime.strptime(start,time_format) + timedelta(minutes=CLASS_DURATION)).strftime(time_format)

        timer(end)

        try:
            driver.close()
        except NoSuchWindowException:           #doesnot create an exception if the user has forcefully exited the class
            pass

        driver.switch_to_window(blackboard_tab)
        driver.find_element_by_class_name('bb-close').click()