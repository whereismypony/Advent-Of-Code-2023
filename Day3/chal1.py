import re

# read file
with open('Day3\input.txt') as f:
    # make a list of the file, for every line an item
    lines = f.readlines()

    

    for line in lines:
        match = re.search(r'\d+',line)
        print('start and end index', match)
        break
    # use a for loop and look for a symbol 

    # get location of symbol in line

    # check if there is a number before or after the symbol

    # go back a line and check if there is a number before or after the same position

    # go forth a line and check if there is a number before or after the same position

