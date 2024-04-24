"""
Add combo version 4
Added the double check of entire combo details, as I forgot to do this earlier.
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
            new_price = easygui.enterbox("What is the new price of the item?\n"
                                         f"The original price was ${old_price}",
                                         "New price")
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
add_combo(combo_dict)
print(combo_dict)
