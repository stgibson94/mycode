#!/usr/bin/env python3

""" script to print to screen in color | Author stgibson94 """

# import colors lib
import crayons

# define the main function
def main():
    # prompt user for favorite color
    fav = 'red'
    fav = str(input("What is you favorite color?"))
    if fav == 'red':
        print(crayons.red('red string'))
    
    elif fav == 'green':
        print(crayons.green('green string'))
    
    elif fav == 'yellow':
        print(crayons.yellow('yellow string'))
    
    elif fav == 'blue':
        print(crayons.blue('blue string'))
    
    elif fav == 'magenta':
        print(crayons.magenta('magenta string'))
    
    elif fav == 'cyan':
        print(crayons.cyan('cyan'))
    
    else:
        print("sorry, color not available")
    
    # print green yellow red on seperate lines
    print(crayons.green('greeen', bold=True))
    print(crayons.yellow('yellow', bold=True))
    print(crayons.red('redred', bold=True))
    
    # prompt user for name
    first = 'first'
    last = 'last'
    first = str(input("What is your first name?"))
    last = str(input("What is your last name?"))
    print(crayons.blue(first), crayons.green(last))

# call the main function
main()
