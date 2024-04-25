"""
Output all version 1
Takes all combos in the menu and outputs them to the Python console.
Also calculates and outputs total prices for each combo.
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

# printing all combos
for combo_ID, combo_inf in combo_dict.items():
    info_list = []
    total_price = 0
    for key in combo_inf:
        info_list.append(f"{key} : ${combo_inf[key]}")
        total_price += float(combo_inf[key])
    combo_info = "\n".join(info_list)
    total_price = f"{total_price:.2f}"
    print(f"Combo ID: {combo_ID}\n"
          f"{combo_info}\n"
          f"Total price of combo items: ${total_price}\n")
