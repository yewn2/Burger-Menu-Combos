"""
Delete combo version 3
Code from version 1 placed in a function
Easygui added
"""

# imports
import easygui


def delete_combo(menu):
    # check if combo in menu
    combo_found = False

    # asking user for ID of combo to delete
    del_ID = easygui.enterbox("Enter the ID of the combo you want to delete:",
                              "Combo ID")

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

delete_combo(combo_dict)

print(combo_dict)
