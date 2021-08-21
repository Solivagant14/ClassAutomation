#this file has the class which is the blue print for all the classes

from tools import logedin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
from driver import driver,wait
from data import CLASS_DURATION,LAB_DURATION
from selenium.common.exceptions import TimeoutException,NoSuchWindowException

class Course:
    def __init__(self,title,id):
        self.title = title      #title of the class
        self.id = id            #id of the WebElement

    def attend(self,first,start):
        driver.maximize_window()
        while True:
            try:
                driver.find_element_by_id(self.id).click()                                                          #clicks the course
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

        if first:
            while True:                 #this deals with the video and audio check
                try:
                    wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='dialog-description-audio']/div[2]/button"))).click()
                    time.sleep(5)
                    wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='techcheck-video-ok-button']"))).click()
                    break
                except TimeoutException:
                    driver.refresh
            while True:                 #this deals with the tutorial announcement
                try:
                    wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='announcement-modal-page-wrap']/div/div[4]/button"))).click()
                    time.sleep(2)
                    break
                except TimeoutException:
                    driver.refresh()
            try:
                wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='tutorial-dialog-tutorials-menu-learn-about-tutorials-menu-close']"))).click()
            except TimeoutException:
                driver.refresh()

        if 'Lab' in self.title:             #lab timer
            while True:
                if time.time() - start >= LAB_DURATION*60:
                    break
                time.sleep(1)
        else:                               #normal class timer
            while True:
                if time.time() - start >= CLASS_DURATION*60:
                    break
                time.sleep(1)
        try:
            driver.close()
        except NoSuchWindowException:           #doesnot create an exception if the user has forcefully exited the class
            pass

        driver.switch_to_window(blackboard_tab)
        driver.find_element_by_class_name('bb-close').click()