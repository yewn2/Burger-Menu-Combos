"""
Delete combo version 1
This version uses a dictionary, for trialling
Easygui not added
Code not in a function yet
"""

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

# check if combo in menu
combo_found = False

# asking user for ID of combo to delete
del_ID = input("Enter the ID of the combo you want to delete: ")

# check if the combo exists
for combo_ID in combo_dict:
    if del_ID == combo_ID:
        combo_found = True

if not combo_found:
    print("Combo not in menu.")

if combo_found:
    # when combo is found, confirm deletion
    delete = input(f"You would like to delete the combo {del_ID}. "
                   f"Correct? (enter y/n) ")

    # confirmed, remove combo from dictionary and print it out
    if delete == "y":
        # print
        for combo_ID, combo_info in combo_dict.items():
            info_list = []
            for key in combo_info:
                info_list.append(f"{key} : ${combo_info[key]}\n")
            if combo_ID == del_ID:
                print(f"The combo you have deleted is:\n"
                      f"Combo ID: {del_ID}")
                print("".join(info_list))

        # delete
        del combo_dict[del_ID]


print(combo_dict)
