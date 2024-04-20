"""
Version 1 - Burger Menu Combo base component
Compiled welcome_instructions, action_screen
Added unwritten action functions
"""


# imports
import easygui


# function to format instructions
def welcome_instructions(program_name, instruction_list):
    # display welcome screen
    easygui.msgbox(f"Welcome to {program_name}!", "Welcome")

    # display instructions
    instructions = [f"Instructions for use of {program_name}\n"]
    for inst in instruction_list:
        instructions.append(f"\n* {inst} *")
    easygui.msgbox("".join(instructions), "Instructions")


# function to choose action
def action_screen(combos):
    # display action screen with choices
    choice = easygui.buttonbox("What would you like to do?",
                               "BURGER MENU COMBO EDITOR",
                               ["Add combo", "Delete combo",
                                "Find combo", "Output all", "Exit"])

    # while loop to continue asking for choices
    while choice != "Exit":
        # # check the choice and call the appropriate function
        if choice == "Add combo":
            add_combo(combos)
        elif choice == "Delete combo":
            del_combo(combos)
        elif choice == "Find combo":
            find_combo(combos)
        elif choice == "Output all":
            print_all(combos)

        # display action screen with choices again
        choice = easygui.buttonbox("What would you like to do?",
                                   "BURGER MENU COMBO EDITOR",
                                   ["Add combo", "Delete combo",
                                    "Find combo", "Output all", "Exit"])

    # if exit chosen then display ending
    easygui.msgbox("Thanks for using Burger Menu Combo Editor",
                   "Goodbye!")


# unwritten choice functions
def add_combo(menu):
    ...


def del_combo(menu):
    ...


def find_combo(menu):
    ...


def print_all(menu):
    ...


# Main routine goes here:

# printing instructions
welcome_instructions("Burger Menu Combos",
                     ["Choose an action after this box",
                      "To add a combo: enter a combo ID, the items in the "
                      "combo and their respective prices, then confirm "
                      "your entry.",
                      "To delete a combo, enter the combo ID and confirm your "
                      "choice.",
                      "To find a combo, enter the specific combo ID.",
                      "'Output all' allows you to see which combos are already "
                      "present in the menu.",
                      "Once you have finished, exit the program."])

# setting up initial menu
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

# beginning the action choices loop
action_screen(combo_dict)
