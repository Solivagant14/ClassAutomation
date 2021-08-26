#the executable file

from src.schedule import get_schedule
from src.selection import get_todays_classes

get_todays_classes()                #gets todays classes
get_schedule()                      #gets the schedule

from src.driver import driver
from src.course import Course
from src.data import schedule,course_list
from src.schedule import run_schedule
from src.tools import login,clear_screen
from selenium.common.exceptions import WebDriverException

clear_screen()
print("Class Automation Initiated\n")

def keys_to_instance():
    for each in schedule.copy():        #changes the key of schedule to be instance of the class Course
            schedule[Course(each,course_list[each])] = schedule.pop(each)

login()                 
keys_to_instance()
run_schedule()
driver.quit()