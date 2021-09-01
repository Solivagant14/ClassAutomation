from os import name
from .data import course_dict

if name == 'nt':
    from tkinter import Tk,IntVar,Checkbutton,Button,TOP,W
    
    def select_semester_classes():
        root = Tk()
        course_variable = dict()

        def submit():
            for key in course_dict.copy():
                if course_variable[key].get() == 0:
                    del course_dict[key]
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

    def select_semester_classes():
        terminal_menu = TerminalMenu(
            course_dict,
            title="-------------------- Select this Semester Classes --------------------",
            multi_select=True,
            show_multi_select_hint=True,
            multi_select_cursor_style=("fg_blue", "bold"),
            menu_cursor_style=("fg_purple",),
            status_bar_style=("fg_cyan",),
            multi_select_select_on_accept=False,
            clear_screen=True
        )
        terminal_menu.show()
        
        for course in course_dict.copy():
            if course not in terminal_menu.chosen_menu_entries:
                del course_dict[course]