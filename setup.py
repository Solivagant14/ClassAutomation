#setup file to take all the details once from the user

from stp.data import login_dict, course_dict, duration
import json

if __name__ == "__main__":
    login_dict["username"] = input("Username : ")
    login_dict["password"] = input("Password : ")
    with open("./JSONfiles/login.json", "w") as login_json:                          #stores the login details to a json file
        json.dump(login_dict,login_json,indent=4)

from stp.tools import login,get_classes,clear_screen
from stp.selection import select_semester_classes
from stp.driver import driver

if __name__ == "__main__":
    try:
        login()
        get_classes()
        select_semester_classes()
        with open("./JSONfiles/courselist.json", "w") as courselist:            #stored the courselist details to a json file
            json.dump(course_dict, courselist, indent=4)
        
        print("Duration you want to attend in minutes (Ex. : 60)")
        duration["class duration"] = int(input("Class Duration : "))
        duration["lab duration"] = int(input("Lab Duration   : "))
        with open("./JSONfiles/duration.json", "w") as duration_file:          #stores the duration details in a json file
            json.dump(duration, duration_file, indent=4)
        clear_screen()
    except:
        print("Oops! Something went wrong. Please retry")
        driver.quit()