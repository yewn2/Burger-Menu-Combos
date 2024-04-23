"""
Delete combo version 1
This version uses a list, for trialling
Easygui not added
Code not in a function yet
"""

# setting up initial menu
combo_lst = [["Value", ["Beef Burger", "5.69"], ["Fries", "1.00"],
              ["Fizzy Drink", "1.00"]],
             ["Cheezy", ["Cheeseburger", "6.69"], ["Fries", "1.00"],
              ["Fizzy Drink", "1.00"]],
             ["Super", ["Cheeseburger", "6.69"], ["Large fries", "2.00"],
              ["Smoothie", "2.00"]]]

# check if combo in menu
combo_found = False

# asking user for ID of combo to delete
del_ID = input("Enter the ID of the combo you want to delete: ")

# check if the combo exists
combo_index = 0
for combo_ID in combo_lst:
    if del_ID == combo_ID[0]:
        combo_found = True
        combo_index = combo_lst.index(combo_ID)

if not combo_found:
    print("Combo not in menu.")

if combo_found:
    # when combo is found, confirm deletion
    delete = input(f"You would like to delete the combo {del_ID}. "
                   f"Correct? (enter y/n) ")
    # confirmed, remove combo from list and print it out
    if delete == "y":
        # print
        removed_combo = ""
        items_lst = []
        for item in combo_lst[combo_index]:
            items_lst.append(item)
        for item in items_lst:
            removed_combo = "".join(f"{items_lst}")
        print("The combo you have deleted is:")
        print(removed_combo)

        # delete
        combo_lst.pop(combo_index)


print(combo_lst)
