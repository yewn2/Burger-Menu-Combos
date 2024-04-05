"""
Component 2 (Action choices) v2
Places version 1 into a function for easier use in future
Adds calls for choice functions (commented out for now)
"""


# imports
import easygui


def action_screen():
    # display action screen with choices
    choice = easygui.buttonbox("What would you like to do?",
                               "BURGER MENU COMBO EDITOR",
                               ["Add combo", "Delete combo",
                                "Find combo", "Output all", "Exit"])

    # while loop to continue asking for choices
    while choice != "Exit":
        # display action screen with choices
        choice = easygui.buttonbox("What would you like to do?",
                                   "BURGER MENU COMBO EDITOR",
                                   ["Add combo", "Delete combo",
                                    "Find combo", "Output all", "Exit"])

        # # check the choice and call the appropriate function
        # if choice == "Add combo":
        #     add_combo()
        # elif choice == "Delete combo":
        #     del_combo()
        # elif choice == "Find combo":
        #     find_combo()
        # elif choice == "Output all":
        #     print_all()

    # if exit chosen then display ending
    easygui.msgbox("Thanks for using Burger Menu Combo Editor",
                   "Goodbye!")
