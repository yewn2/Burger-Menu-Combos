"""
Add combo version 1
Preliminary code, no function for now.
Easygui not yet added.
Asks user to enter ID, items and prices then confirms.
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

# add ID to dictionary
combo_dict[new_ID] = {}


# entering items and prices
again = "y"
while again == "y":
    new_item = input("Enter the name of the item you wish to add: ")
    item_price = float(input(f"Enter the price of {new_item}: "))
    item_price = f"{item_price:.2f}"
    # confirmation
    item_confirmed = input(f"The item you wish to add is {new_item}, "
                           f"with a price of ${item_price}. "
                           f"Enter y/n to confirm: ").lower()
    if item_confirmed != "y":
        again = "y"
    else:
        combo_dict[new_ID][new_item] = item_price
        again = input("Do you want to add another item? Enter y/n: ")


print(combo_dict)
