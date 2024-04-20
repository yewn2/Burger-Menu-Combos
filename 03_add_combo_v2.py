"""
Add combo version 2
Trialling add combo with a list instead of a dictionary
"""

# setting up initial menu
combo_lst = [["Value", ["Beef Burger", "5.69"], ["Fries", "1.00"],
              ["Fizzy Drink", "1.00"]],
             ["Cheezy", ["Cheeseburger", "6.69"], ["Fries", "1.00"],
              ["Fizzy Drink", "1.00"]],
             ["Super", ["Cheeseburger", "6.69"], ["Large fries", "2.00"],
              ["Smoothie", "2.00"]]]

# entering ID
new_ID = input("Enter an ID for your new combo: ")

# ID confirmation
confirm_ID = input(f"The ID you want to have for your new combo is '{new_ID}'. "
                   f"Enter y/n to confirm: ").lower()
while confirm_ID != "y":
    new_ID = input("Enter an ID for your new combo: ")
    confirm_ID = input(
        f"The ID you want to have for your new combo is '{new_ID}'. "
        f"Enter y/n to confirm: ").lower()

# add ID to list and check position
combo_lst.append([])
combo_index = combo_lst.index([])
combo_lst[combo_index].insert(combo_index, new_ID)

# ask for number of items needed to add
item_num = int(input(f"How many items would you like to add "
                     f"to the combo {new_ID}? "))

# entering items and prices
item_index = 1
while item_index <= item_num:
    new_item = input("Enter the name of the item you wish to add: ")
    item_price = float(input(f"Enter the price of {new_item}: "))
    item_price = f"{item_price:.2f}"
    # confirmation
    item_confirmed = input(f"The item you wish to add is {new_item}, "
                           f"with a price of ${item_price}. "
                           f"Enter y/n to confirm: ").lower()
    if item_confirmed != "y":
        item_index = item_index
    else:
        combo_lst[combo_index].insert(item_index, [new_item, item_price])
        item_index += 1

print(combo_lst)
