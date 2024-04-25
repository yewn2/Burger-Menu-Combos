"""
Version 2 - Burger Menu Combo base component
Added two action functions - add combo and delete combo
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
            delete_combo(combos)
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


# function to add combo
def add_combo(menu):
    # entering ID
    new_ID = easygui.enterbox("Enter an ID for your new combo:",
                              "New ID")

    # ID confirmation
    confirm_ID = easygui.buttonbox(f"The ID you want to have for your new "
                                   f"combo is '{new_ID}'.",
                                   "ID Confirmation",
                                   ["Yes", "No"])
    while confirm_ID != "Yes":
        new_ID = easygui.enterbox("Enter an ID for your new combo:",
                                  "New ID")
        confirm_ID = easygui.buttonbox(f"The ID you want to have for your new "
                                       f"combo is '{new_ID}'.",
                                       "ID Confirmation",
                                       ["Yes", "No"])

    # add ID to dictionary
    menu[new_ID] = {}

    # entering items and prices
    again = "Yes"
    while again == "Yes":
        new_item = easygui.enterbox("Enter the name of the item you wish to "
                                    "add:", "New Item")
        item_price = float(easygui.enterbox(f"Enter the price of {new_item}:",
                                            f"{new_item} Price"))
        item_price = f"{item_price:.2f}"
        # confirmation
        item_confirmed = easygui.buttonbox(
            f"The item you wish to add is {new_item}, "
            f"with a price of ${item_price}.",
            "Confirm Item", ["Yes", "No"])
        if item_confirmed != "Yes":
            again = "Yes"
        else:
            menu[new_ID][new_item] = item_price
            again = easygui.buttonbox("Do you want to add another item?",
                                      "Add Again?", ["Yes", "No"])

    # double check combo with user
    combo_confirm = ""
    for combo_ID, combo_inf in menu.items():
        info_list = []
        for key in combo_inf:
            info_list.append(f"{key} : ${combo_inf[key]}")
        if combo_ID == new_ID:
            combo_info = "\n".join(info_list)
            combo_confirm = easygui.buttonbox(
                "Would you like to change any items in "
                f"the combo {new_ID}?\n"
                f"{combo_info}", "Confirm combo",
                ["Yes", "No"])

    # if change wanted, ask for item to change
    while combo_confirm == "Yes":
        item_change = easygui.enterbox("Which item would you like to change?")
        old_price = 0
        item_found = False
        # search for the item
        for combo_ID, combo_inf in menu.items():
            for key in combo_inf:
                if key == item_change:
                    item_found = True
                    old_price = combo_inf[key]
        if not item_found:
            easygui.msgbox("Sorry, that item does not exist.",
                           "Item not found")
        # if the item is found
        else:
            new_item = easygui.enterbox("What would you like to change the "
                                        f"item {item_change} to?",
                                        "New item")
            new_price = float(easygui.enterbox("What is the new price of the "
                                               "item?\n"
                                               f"The original price was "
                                               f"${old_price}",
                                               "New price"))
            new_price = f"{new_price:.2f}"
            del menu[new_ID][item_change]
            menu[new_ID][new_item] = new_price

        # double check combo with user
        for combo_ID, combo_inf in menu.items():
            info_list = []
            for key in combo_inf:
                info_list.append(f"{key} : ${combo_inf[key]}")
            if combo_ID == new_ID:
                combo_info = "\n".join(info_list)
                combo_confirm = easygui.buttonbox(
                    "Would you like to change any items in "
                    f"the combo {new_ID}?\n"
                    f"{combo_info}", "Confirm combo",
                    ["Yes", "No"])


# function to delete combo
def delete_combo(menu):
    # check if combo in menu
    combo_found = False

    # asking user for ID of combo to delete
    del_ID = easygui.enterbox("Enter the ID of the combo you want to delete:",
                              "Combo ID")

    # ID confirmation
    confirm_ID = easygui.buttonbox(f"The ID of the combo you want to "
                                   f"delete is '{del_ID}'.",
                                   "ID Confirmation",
                                   ["Yes", "No"])
    while confirm_ID != "Yes":
        del_ID = easygui.enterbox(
            "Enter the ID of the combo you want to delete:",
            "Combo ID")
        confirm_ID = easygui.buttonbox(f"The ID of the combo you want to "
                                       f"delete is '{del_ID}'.",
                                       "ID Confirmation",
                                       ["Yes", "No"])
    # check if the combo exists
    for combo_ID in menu:
        if del_ID == combo_ID:
            combo_found = True

    if not combo_found:
        easygui.msgbox("Combo not in menu.", "Combo not found")

    if combo_found:
        # when combo is found, confirm deletion
        delete = easygui.buttonbox(f"You would like to delete "
                                   f"the combo {del_ID}.",
                                   "Confirm delete", ["Yes", "No"])

        # confirmed, remove combo from dictionary and print it out
        if delete == "Yes":
            # print
            for combo_ID, combo_inf in menu.items():
                info_list = []
                for key in combo_inf:
                    info_list.append(f"{key} : ${combo_inf[key]}")
                if combo_ID == del_ID:
                    combo_info = "\n".join(info_list)
                    easygui.msgbox(f"The combo you have deleted is:\n"
                                   f"{del_ID}\n"
                                   f"{combo_info}", "Deleted combo")

            # delete
            del menu[del_ID]


# function to find combo
def find_combo(menu):
    ...


# function to print all combos
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
