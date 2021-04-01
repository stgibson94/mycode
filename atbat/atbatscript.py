#!usr/bin/env python3

""" AT-Bat 2 Player Game | Authour stgibson94 """

# imports
import sys


# define the main function
def main():
    
    # print title of game
    print("Welcome to AT-Bat!\n(2 Players Required)")
    
    # create pitch lists
    loc = [input("Enter pitch 1 location (ball or strike): "),input("Enter pitch 2 location: "),input("Enter pitch 3 location: "),input("Enter pitch 4 location: "),input("Enter pitch 5 location: "),input("Enter pitch 6 location: ")]
    ball = [input("Enter pitch 1 type (fast or slow): "),input("Enter pitch 2 type: "),input("Enter pitch 3 type: "),input("Enter pitch 4 type: "),input("Enter pitch 5 type: "),input("Enter pitch 6 type: ")]

    print(loc)
    print(ball)
    
    # prompt player 2 to swing or take and guess pitch if swinging (happens for every pitch)
    guess1 = 'ball'
    guess2 = 'fast'
    counter = 0             # counter for pitches list

    # while for full at bat
    while counter < 7:
        counter += 1
        print("Here comes pitch" + counter + "!")
        guess1 = input("Guess the pitch location (ball or strike): ")
        
        # if for the at bat sequence
        #if guess1 == 'strike':
            #guess2 = input("Guess the pitch type: ")
            #print("Batter swings!")
            #if guess2 == ball[counter]
            #print("Hit!")
            #else:
             #   print("Strike")
        #else:
         #   print("Batter takes")
          #  if ball[counter] == 'ball':
           #     print('Ball')
            #else:
             #   print('Strike')
            
        print(counter)


# end the main function
if __name__ == '__main__':
    main()
