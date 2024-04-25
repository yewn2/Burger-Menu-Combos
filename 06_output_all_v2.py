"""
Output all version 2
Code placed into a function
"""


def print_all(menu):
    # printing all combos
    for combo_ID, combo_inf in menu.items():
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
