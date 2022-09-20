#!/usr/bin/env python3

def main():

    # define the initial empty list
    animals = ["Fox", "Fly", "Ant", "Dog", "Cat"]

    # define user command, initially this is empty
    user_command = ""
    
    # print messages that explain how the program works
    print("You can add or remove a three-letter animal in your list")
    print("Also, you may reverse the list")
    print("To do so, simply enter add, remove, or reverse")
    print("To quit, enter quit")

    # while user command is not quit, show the current list of animals and prompt the user to enter a command
    while user_command != "quit":
        
        # print the current list of animals
        print(f"Your current list: {animals}")
        
        # prompt the user to enter a command
        user_command = input("What would you like to do? ")
    
        # if user command is add, prompt the user to enter the animal name
        if user_command == "add":
            animal = ""

            # while user's input animal's length is not 3, keep prompt them to enter an animal
            while len(animal) != 3:
                animal = input("What animal would you like to add? (has to be three-letter name animal) ")
            # add the user's input animal to the animals list
            animals.append(animal.capitalize())

        # if user command is remove, remove the desired animal
        if user_command == "remove":
            animal = input("What animal would you like to remove? ")
            animals.remove(animal.capitalize())
        
        # if the user command is reverse, reverse the animals list
        if user_command == "reverse":
            animals.reverse()

main()
