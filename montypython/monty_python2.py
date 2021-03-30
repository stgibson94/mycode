#!/usr/bin/env python3

# create counter
round = 0

# simple while loop that will run until a break is executed
while True:
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")
    if answer == 'Brian':
        print('Correct')
        break
    elif round == 3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry, try again!")
