"""
Component 1 (Welcome screen and instructions) v2
Takes welcome_instructions v1 and places it into a function for easier use
Instructions and program name variables added for easier function use in future
"""

# imports
import easygui


def welcome_instructions(program_name, instruction_list):
    # display welcome screen
    easygui.msgbox(f"Welcome to {program_name}!", "Welcome")

    # display instructions
    instructions = [f"Instructions for use of {program_name}\n"]
    for inst in instruction_list:
        instructions.append(f"\n* {inst} *")
    easygui.msgbox("".join(instructions), "Instructions")


# Main routine goes here:
welcome_instructions("Burger Menu Combos",
                     ["Choose an action after this box",
                      "To add a combo: enter a combo ID, the items in the "
                      "combo and their respective prices, then confirm "
                      "your entry.",
                      "To delete a combo, enter the combo ID and confirm your "
                      "choice.",
                      "To find a combo, enter the specific combo ID.",
                      "'Output all' allows you to see which combos are already "
                      "present in the menu.",
                      "Once you have finished, exit the program."])
