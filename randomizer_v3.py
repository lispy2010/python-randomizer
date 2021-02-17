import random # Importing random-library
def program():
    print("Welcome to Randomizer 3.0!")
    print("Type \"START\" to start randomizing, or \"HELP\", if you need help with this program.")
    ych = input("Insert your choice here: ") # Reading variable "ych"
    if ych == "START": # If ych equals "START"
        print("You selected START!")
        first = input("Enter first word: ") # Reading first word
        second = input("Enter second word: ")  # Reading second word
        third = input("Enter third word (if it's nothing, leave blank): ") # Reading third word
        if third != "": # If third isn't ""
            fourth = input("Enter fourth word (if it's nothing, leave blank): ") # Reading fourth word
            if fourth != "": # If fourth isn't ""
                fifth = input("Enter fifth word (if it's nothing, leave blank): ") # Reading fifth word
                if fifth != "": # If fifth isn't ""
                    print("Randomizer selected " + random.choice([first, second, third, fourth, fifth]) + "!") # Result message
                else:
                    print("Randomizer selected " + random.choice([first, second, third, fourth]) + "!") # Result message
            else:
                print("Randomizer selected " + random.choice([first, second, third]) + "!") # Result message
        else:
            print("Randomizer selected " + random.choice([first, second]) + "!") # Result message
        yon2 = input("Another randomization? (y/n): ") # Reading yon2
        if yon2 == "y": # If yon2 equals "y"
             program() # Go to the beginning
        elif yon2 == "n": # If yon2 equals "n"
            input("See you later! But now, goodbye!") # Inputs "See you later! But now, goodbye!"
        else:
            print("A rousing error.") # Error message
            
    elif ych == "HELP": # If ych equals "HELP"
        print("""
---HELP---
How to use Randomizer?
1. Insert 1st word and 2nd word;
2. If you need, enter 3rd, 4th etc;
3. Read returned result.
(C) 2020 Lys15YT. Powered by Python 3.8-32.
""")
        input("Press enter to continue...") # Inputs "Press enter to continue..."
        program() # Going to main menu
    else:
        program() # Going to main menu


program() # Program starting
