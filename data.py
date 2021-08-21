#program to store and initialize all the data so that it can be accessed by the whole project

import json

with open('./JSONfiles/login.json', 'r') as json_file:          #reading the stored login details
    login = json.load(json_file)
    USERNAME = login['username']
    PASSWORD = login['password']

with open('./JSONfiles/courselist.json','r') as json_file:      #reading the stored courselist details
    course_list = json.load(json_file)

todays_courses = list()
schedule = dict() 

with open("./JSONfiles/durations.json", "r") as duration_file:  #reading the stored durations details
    durations = json.load(duration_file)
    CLASS_DURATION = durations["class duration"]
    LAB_DURATION = durations["lab duration"]