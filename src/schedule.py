#file that deals with the schedule

from .data import todays_courses,schedule,time_format
import time

def get_schedule():                                             #gets schedule from the user for today
    for course in todays_courses:
        schedule[course] = ''

    print('\nEnter the Schedule of the Classes in HH:MM\n')
    for each in schedule:
        print(each,'\t-\t',end='')
        schedule[each] = input()
    print('\n')

def run_schedule():                                             #runs the schedule for today
    first = True        #flag for the first time logging in

    while bool(schedule):
        current_time = time.strftime(time_format)
        for course in schedule.copy():
            if schedule[course] <= current_time:
                course.attend(first,schedule[course])
                first = False       #flags down
                del schedule[course]    #deletes the class from schedule from attended
        time.sleep(1)

    print("\nEnd of Today's Sesion\n")