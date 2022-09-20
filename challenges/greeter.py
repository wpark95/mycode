#!/usr/bin/env python3

def main():

    # pause the program and wait for the user to provide their name
    user_name = input("Hey there! What is your name? ")

    # capitalize the user's name
    user_name = str.capitalize(user_name)

    # define function that checks if the user's name contains number
    def name_has_number(name):
        return any(char.isdigit() for char in name)

    # if the name contains number, print out a funny greeting message. Otherwise, print regular greeting message
    if(name_has_number(user_name)):
        print(f"Nice name you got {user_name}! Did Elon Musk name you?")
    else:
        print(f"I hope you're doing well {user_name}, wherever you are!")

    # pause the program and wait for the user to provide the day of the week
    user_day = input("What day of the week is it there? ")

    # capitalize the day of the week
    user_day = str.capitalize(user_day)

    # finally, print out a greeting message with user name and the day of the week
    print(f"Hello, {user_name}! Happy {user_day}!")

main()
