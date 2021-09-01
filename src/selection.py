from os import name
from .data import course_dict,todays_courses

if name == 'nt':                                                #tkinter for Windows
    from tkinter import Tk,IntVar,Checkbutton,Button,Label,TOP,W
    
    def select_todays_classes():
        root = Tk()
        course_variable = dict()

        def submit():
            for key in course_dict.copy():
                if course_variable[key].get() == 1:
                    todays_courses.append(key)
            root.destroy()
        
        label = Label(root, text="Select the Classes you need this Semester")
        label.pack(pady=10)

        for course in course_dict:
            course_variable[course] = IntVar()
            l = Checkbutton(root, text=course, variable=course_variable[course] )
            l.pack(pady=2, side=TOP, anchor=W)
        submit = Button(root,text="Submit",command=submit)
        submit.pack(pady=10)

        root.mainloop()

else:                                                           #simple term menu for linux and mac
    from simple_term_menu import TerminalMenu
    def select_todays_classes():
        
        terminal_menu = TerminalMenu(
            course_dict,
            title="-------------------- Select Today's Classes --------------------",
            multi_select=True,
            show_multi_select_hint=True,
            multi_select_cursor_style=("fg_blue", "bold"),
            menu_cursor_style=("fg_purple",),
            status_bar_style=("fg_cyan",),
            multi_select_select_on_accept=False,
            clear_screen=True
        )
        terminal_menu.show()
        
        for course in course_dict:
            if course in terminal_menu.chosen_menu_entries:
                todays_courses.append(course)