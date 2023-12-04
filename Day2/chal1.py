maxRed = 12
maxGreen = 13
maxBlue = 14
possibleGames = 0

with open('Day2\input.txt') as f:
    lines = f.readlines()

    for line in lines:
        possible = True
        gameID = line.split(':')[0].split()[1]
        gameData = line.split(':')[1]
        rounds = gameData.split(';')
        for round in rounds:
            hands = round.split(',')
            for hand in hands:
                amount = hand.split()[0]
                color = hand.split()[1]
                match color:
                    case 'red':
                        if(int(amount) > maxRed):
                            possible = False
                    case 'green':   
                        if(int(amount) > maxGreen):
                            possible = False 
                    case 'blue':
                        if(int(amount) > maxBlue):
                            possible = False

            if(not possible): break
                
        if(possible): possibleGames += int(gameID)
            
                 

print(possibleGames)             


