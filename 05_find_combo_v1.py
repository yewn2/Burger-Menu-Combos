"""
Find combo version 1
This code is essentially the 'delete_combo' function, but does not find a
combo, just prints it out.
Therefore, I have copied over the delete_combo function and changed/removed
some of the code.
"""

# imports
import easygui


def find_combo(menu):
    # check if combo in menu
    combo_found = False

    # asking user for ID of combo to find
    find_ID = easygui.enterbox("Enter the ID of the combo you want to find:",
                               "Combo ID")

    # ID confirmation
    confirm_ID = easygui.buttonbox(f"The ID of the combo you want to "
                                   f"find is '{find_ID}'.",
                                   "ID Confirmation",
                                   ["Yes", "No"])
    while confirm_ID != "Yes":
        find_ID = easygui.enterbox(
            "Enter the ID of the combo you want to find:",
            "Combo ID")
        confirm_ID = easygui.buttonbox(f"The ID of the combo you want to "
                                       f"find is '{find_ID}'.",
                                       "ID Confirmation",
                                       ["Yes", "No"])
    # check if the combo exists
    for combo_ID in menu:
        if find_ID == combo_ID:
            combo_found = True

    # combo not found?
    if not combo_found:
        easygui.msgbox("Combo not in menu.", "Combo not found")

    # combo found?
    if combo_found:
        # print out combo
        for combo_ID, combo_inf in menu.items():
            info_list = []
            for key in combo_inf:
                info_list.append(f"{key} : ${combo_inf[key]}")
            if find_ID == combo_ID:
                combo_info = "\n".join(info_list)
                easygui.msgbox(f"The combo you have found is:\n"
                               f"{find_ID}\n"
                               f"{combo_info}", "Found combo")
