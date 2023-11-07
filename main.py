import random

options = ["simple equations", "linear equations", "addition", "subtraction", "division", "multiplication"]

inp = input(f"Enter practice question type {options}: ")

if inp in options:
    if inp == "simple equations":
        pass
    elif inp == "linear equations":
        pass
    elif inp == "addition":
        difficulty = ['easy', 'medium', 'hard']
    elif inp == "subtraction":
        pass
    elif inp == "division":
        pass
    elif inp == "multiplication":
        pass


else:
    print("Please enter a valid option")
