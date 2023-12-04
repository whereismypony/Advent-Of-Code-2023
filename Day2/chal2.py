with open('Day2\input.txt') as f:
    lines = f.readlines()

    result = 0

    for line in lines:
        red = 0
        green = 0
        blue = 0

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
                        if(int(amount) > int(red)):
                            red = amount
                    case 'green':   
                        if(int(amount) > int(green)):
                            green = amount
                    case 'blue':
                        if(int(amount) > int(blue)):
                            blue = amount
        
        result += (int(red) * int(green) * int(blue))
        
    print (result)

