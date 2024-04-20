"""
Add combo version 3
I decided to use the code from version 1 as it would be easier to implement
in my final code.
Placed code in a function
Added Easygui
"""

# imports
import easygui


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
