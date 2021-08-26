#this file has the class which is the blue print for all the classes

from .tools import logedin,check_notice
from .driver import driver,wait10,wait30
from .data import CLASS_DURATION,LAB_DURATION,time_format
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
import threading
from datetime import datetime,timedelta
from selenium.common.exceptions import NoSuchElementException

class Course:
    def __init__(self,title,id):
        self.title = title      #title of the class
        self.id = id            #id of the WebElement
        self.flag = True

    def timer(self,end):
        while self.flag:
            current_time = time.strftime(time_format)
            if current_time >= end:
                driver.close()
                self.flag = False

    def check_tab(self):
        while self.flag:
            try:
                driver.window_handles[1]
            except:
                self.flag = False

    def attend(self,first,start):
        driver.maximize_window()
        while True:
            try:
                driver.find_element_by_id(self.id).click()                                                          #clicks the course
                check_notice()
                wait10.until(ec.presence_of_element_located((By.XPATH, "//*[@id='sessions-list-dropdown']/span")))
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
                    wait10.until(ec.presence_of_element_located((By.XPATH, "//*[@id='dialog-description-audio']/div[2]/button"))).click()
                    time.sleep(5)
                    wait10.until(ec.presence_of_element_located((By.XPATH, "//*[@id='techcheck-video-ok-button']"))).click()
                    break
                except:
                    driver.refresh
            while True:                 #this deals with the tutorial announcement
                try:
                    wait30.until(ec.presence_of_element_located((By.XPATH, "//*[@id='announcement-modal-page-wrap']/div/div[4]/button"))).click()
                    time.sleep(2)
                    break
                except:
                    driver.refresh()
            try:
                wait10.until(ec.presence_of_element_located((By.XPATH, "//*[@id='tutorial-dialog-tutorials-menu-learn-about-tutorials-menu-close']"))).click()
            except:
                driver.refresh()

        end = (datetime.strptime(start,time_format) + timedelta(minutes=LAB_DURATION)).strftime(time_format) if 'Lab' in self.title else (datetime.strptime(start,time_format) + timedelta(minutes=CLASS_DURATION)).strftime(time_format)

        timer_thread = threading.Thread(target=self.timer, args=(end,))         #thread to check the timer
        check_tab_thread = threading.Thread(target=self.check_tab)              #thread to check if the user has closed the class
        timer_thread.start()
        check_tab_thread.start()

        while self.flag:
            pass

        driver.switch_to_window(blackboard_tab)
        driver.find_element_by_class_name('bb-close').click()