"""
Component 2 (Action choices) v2
Places version 1 into a function for easier use in future
Adds calls for choice functions (commented out for now)
"""


# imports
import easygui


def action_screen(combos):
    # display action screen with choices
    choice = easygui.buttonbox("What would you like to do?",
                               "BURGER MENU COMBO EDITOR",
                               ["Add combo", "Delete combo",
                                "Find combo", "Output all", "Exit"])

    # while loop to continue asking for choices
    while choice != "Exit":
        # # check the choice and call the appropriate function
        # if choice == "Add combo":
        #     add_combo(combos)
        # elif choice == "Delete combo":
        #     del_combo(combos)
        # elif choice == "Find combo":
        #     find_combo(combos)
        # elif choice == "Output all":
        #     print_all(combos)

        # display action screen with choices again
        choice = easygui.buttonbox("What would you like to do?",
                                   "BURGER MENU COMBO EDITOR",
                                   ["Add combo", "Delete combo",
                                    "Find combo", "Output all", "Exit"])

    # if exit chosen then display ending
    easygui.msgbox("Thanks for using Burger Menu Combo Editor",
                   "Goodbye!")


# main program
combo_dict = {
    "Value":
        {"Beef Burger": "5.69",
         "Fries": "1.00",
         "Fizzy Drink": "1.00"},
    "Cheezy":
        {"Cheeseburger": "6.69",
         "Fries": "1.00",
         "Fizzy Drink": "1.00"},
    "Super":
        {"Cheeseburger": "6.69",
         "Large fries": "2.00",
         "Smoothie": "2.00"}
}
action_screen(combo_dict)
