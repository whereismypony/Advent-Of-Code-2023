import re

# array is like:
#   y 0 1 2
# x   
# 0   . . *
# 1   . 9 0
# 2   . . .

# read file
with open('Day3\input.txt') as f:
    # make a list of the file, for every line an item and loop through them
    lines = f.readlines()
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            print() 
    
    # use a for loop and look for a symbol 

    # get location of symbol in line

    # check if there is a number before or after the symbol

    # go back a line and check if there is a number before or after the same position

    # go forth a line and check if there is a number before or after the same position
    

    # using a [cursor_position] and [symbol_position]:
    # make a check function that checks all surrounding positions if there is a number in it. If it finds one it can go on to the move left 
    # or right functions to find the beginnen/end of the numbers. If a number is found first move as far left as possible.
    # then note it down while going to the left. 

    # make a look left function that goes on until it finds something else then a number
    # make a look right function that takes the number under the cursor and adds it (as string) until it finds something else than a number

