import random

options = ["simple equations", "linear equations", "addition", "subtraction", "division", "multiplication"]

inp = input(f"Enter practice question type {options}: ")

if inp in options:
    pass
else:
    print("Please enter a valid option")
