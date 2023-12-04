import re

spelledNumbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, }
total = 0

def getFirstInt(string):
    return re.search(r'\d+',string).group()

# Read Input of input.txt
with open('Day1\input.txt') as f:
    lines = f.readlines()
    for line in lines:
        first = ""
        last = ""
        currentPosFirst = 999
        currentPosLast = 999
        
        # find first number in string (writen)
        for number in spelledNumbers:
            pos = line.find(number)
            if(pos >= 0 and pos < currentPosFirst):
                currentPosFirst = pos
                first = spelledNumbers[number]

        # find first number in string
        pos = line.find(getFirstInt(line)[0])
        if(pos >= 0 and pos < currentPosFirst):
            currentPosFirst = pos
            first = getFirstInt(line)[0]

        # find Last number in string (writen)
        for number in spelledNumbers:
            pos = line[::-1].find(number[::-1])
            if(pos >= 0 and pos < currentPosLast):
                currentPosLast = pos
                last = spelledNumbers[number]

        # find Last number in string
        pos = line[::-1].find(getFirstInt(line[::-1])[0])
        if(pos >= 0 and pos < currentPosLast):
            currentPosLast = pos
            last = getFirstInt(line[::-1])[0]   
        
        total += int(str(first) + str(last))
    
    print(" TOTAL: {}".format(total))