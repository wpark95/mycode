#!/usr/bin/env python3

def main():

    # Initial list (empty)
    user_list = []

    # Prompt the user to enter a command
    print("You can add or remove an item to your list or reverse the list")

    print("To do so, simply enter either add, remove, or reverse")

    print ("To quit, simply enter quit")
    
    # Initial command (empty string)
    user_command = ""
    
    # While user command is not quit, keep prompting them to enter a command and an item
    while user_command != "quit":
        
        print(f"Your list: {user_list}")

        user_command = input("What would you like to do? ")
    
        if user_command == "add":
            item = input("What would you like to add? ")
            user_list.append(item)

        if user_command == "remove":
            item = input("what would you like to remove? ")
            user_list.remove(item)
    
        if (user_command == "reverse"):
            user_list.reverse()

main()
