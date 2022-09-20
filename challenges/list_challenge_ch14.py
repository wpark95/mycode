#!/usr/bin/env python3

""" Prints a message with a student name, based on user input """
def main():

    # import Python's random module
    import random
    
    # list of words that are used in the final print message
    wordbank= ["indentation", "spaces"]

    # list of student names
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    # append the integer 4 to the list wordbank
    wordbank.append(4)

    # prompt the user to answer if they want to choose a number and save response as lowercase to is_random
    is_random = input("Would you like to choose a random student? (y/n) ").lower()

    # placeholder for student_name
    student_name = ""

    # if the user wants a random student, randomly choose a student name from tlgstudents and assign it to student_name
    if is_random == "y":
        
        student_name = random.choice(tlgstudents)
    
    # if the user does not want a random student, prompt them to enter a number and save it as num
    else:

        # prompt the user to enter a number [0 - 18) or a student name
        print("1) enter a number between 0 - 18")
        print("OR")
        print("2) enter the name of a student")

        # then save user input as user_response
        user_response = input("> ")

        # if the user entered a number
        if user_response.isdigit():
            
            # convert the response to an integer then slice an element in the list tlgstudents using the integer and assign it to student_name
            student_name = tlgstudents[int(user_response)]

        # otherwise, if user entered a non-integer, assign their response to student_name
        else: 

            student_name = user_response

    # print a message using student_name
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

main()
