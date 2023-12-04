import re

# the calibration value can be found by combining the first digit and the last digit (in that order)
# to form a single two-digit number
total = 0

def getFirstInt(string):
    return re.search(r'\d+',string).group()

# Read Input of input.txt
with open('Day1\input.txt') as f:
    lines = f.readlines()

    # Go through the rows 1 by 1
    for line in lines:
        first  = ""
        last = ""

        # look for the first digit in the string
        first = getFirstInt(line)[0]

        # look for the lastdigit in the string by reversing the line
        last = getFirstInt(line[::-1])[0]

        # add the digits to the total as int
        total += int(first + last)
        
# print total
print("Total: " + str(total))
