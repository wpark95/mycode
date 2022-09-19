# shebang
#!/usr/bin/env python3

def main():

    # pause the program and wait for the user to provide their name
    user_name = input("Hey there! What is your name? ")
    
    # display the input back to the user.
    print(f"I hope you're doing well {user_name}, wherever you are!")

    # pause the program and wait for the user to provide the day of the week
    user_day = input("What day of the week is it there? ")
    user_day = str.capitalize(user_day)

    print("Hello, " + user_name + "! Happy " + user_day + "!")

main()
