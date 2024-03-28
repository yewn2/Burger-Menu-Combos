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
    instructions = ""
    easygui.msgbox(f"{instructions}", "Instructions")


# Main routine goes here:
