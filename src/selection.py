from os import name
from .data import course_dict,todays_courses

if name == 'nt':
    from tkinter import Tk,IntVar,Checkbutton,Button,TOP,W
    
    def select_todays_classes():
        root = Tk()
        course_variable = dict()

        def submit():
            for course in course_dict():
                if course_variable[course].get() == 1:
                    todays_courses.append(course)
            root.destroy()

        for course in course_dict:
            course_variable[course] = IntVar()
            l = Checkbutton(root, text=course, variable=course_variable[course] )
            l.pack(side=TOP, anchor=W)
        submit = Button(root,text="Submit",command=submit)
        submit.pack()

        root.mainloop()

else:
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