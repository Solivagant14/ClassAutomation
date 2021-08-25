#the executable file

from src.schedule import get_schedule
from src.selection import get_todays_classes

get_todays_classes()                #gets todays classes
get_schedule()                      #gets the schedule

from src.driver import driver
from src.data import course_list,schedule
from src.course import Course
from src.schedule import run_schedule
from src.tools import login

login()                             #logs in
for each in schedule.copy():        #changes the key of schedule to be instance of the class Course
    schedule[Course(each,course_list[each])] = schedule.pop(each)
print("Class Automation Initiated\n")

run_schedule()

# while True:
#     try:
#         run_schedule()              #runs schedule
#         break
#     except KeyboardInterrupt:
#         break
#     except:
#         run_schedule()
        
driver.close()