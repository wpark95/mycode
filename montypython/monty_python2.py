#!/usr/bin/env python3
"""Conditionals - Life of Brian guessing game using a while True loop."""

# integer round initiated to 0
round = 0

# sets up an infinite loop condition
while True:

# increase the round counter
    round += 1

    # print the question
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    
    # prompt the user to guess and save their response
    answer = input("Your guess--> ")

    # logic to check if user gave correct answer
    if answer == 'Brian':

        # print winning message
        print('Correct!')

        # break out of the while loop
        break

    # logic to ensure round has not yet reached 3
    elif round == 3:

        # if round has reached 3, print the correct answer
        print('Sorry, the answer was Brian.')
        
        # break out of the loop
        break

    # if answer was wrong and round is not yet 3
    else:

        # inform the user that their guess was wrong
        print('Sorry. Try again!')

