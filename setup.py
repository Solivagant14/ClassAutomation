#setup file to take all the details once from the user

import json

login_dict = dict()
login_dict["username"] = input("Username : ")
login_dict["password"] = input("Password : ")
with open("./JSONfiles/login.json", "w") as login:                          #stores the login details to a json file
    json.dump(login_dict,login,indent=4)

from tools import get_classes
from selection import get_semester_classes
from data import course_list
from driver import driver

try:
    get_classes()
    driver.quit()
    get_semester_classes()
    with open("./JSONfiles/courselist.json", "w") as courselist:            #stored the courselist details to a json file
        json.dump(course_list, courselist, indent=4)

    durations = dict()
    print("Duration you want to attend in minutes (Ex. : 60)")
    durations["class duration"] = int(input("Class Duration : "))
    durations["lab duration"] = int(input("Lab Duration : "))
    with open("./JSONfiles/durations.json", "w") as duration_file:          #stores the duration details in a json file
        json.dump(durations, duration_file, indent=4)
except:
    print("Oops! Something went wrong. Please retry")
    driver.close()