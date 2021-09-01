#all the fucntions used for command line selection

from simple_term_menu import TerminalMenu
from .data import course_dict

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