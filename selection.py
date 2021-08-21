#all the fucntions used for command line selection

from simple_term_menu import TerminalMenu
from data import course_list
from data import todays_courses

def get_semester_classes():
    
    terminal_menu = TerminalMenu(
        course_list,
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
    
    for course in course_list.copy():
        if course not in terminal_menu.chosen_menu_entries:
            del course_list[course]

def get_todays_classes():
    
    terminal_menu = TerminalMenu(
        course_list,
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
    
    for course in course_list:
        if course in terminal_menu.chosen_menu_entries:
            todays_courses.append(course)