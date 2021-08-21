#the executable file

from schedule import get_schedule
from selection import get_todays_classes

get_todays_classes()                #gets todays classes
get_schedule()                      #gets the schedule

from driver import driver
from data import course_list,schedule
from course import Course
from schedule import run_schedule
from tools import login

login()                             #logs in
for each in schedule.copy():        #changes the key of schedule to be instance of the class Course
    schedule[Course(each,course_list[each])] = schedule.pop(each)
print("Class Automation Initiated\n")
run_schedule()
driver.close()