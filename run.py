#the executable file

from src.schedule import get_schedule,run_schedule
from src.selection import get_todays_classes

if __name__ == '__main__':
    get_todays_classes()                #gets todays classes
    get_schedule()                      #gets the schedule

from src.driver import driver
from src.course import Course
from src.data import schedule,course_list
from src.tools import login,clear_screen

if __name__ == '__main__':
    clear_screen()
    print("Class Automation Initiated\n")
    
    login()                 
    for each in schedule.copy():        #changes the key of schedule to be instance of the class Course
        schedule[Course(each,course_list[each])] = schedule.pop(each)
    run_schedule()
    driver.quit()