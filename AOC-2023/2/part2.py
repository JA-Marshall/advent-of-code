import re

file = open("list.txt","r")
data = file.readlines()
strings = []
for line in data:
    strings.append(line.replace("\n",""))

calibration_codes = []
sum = 0
i = 0



def check_strings(string):
    print(f'Game:{i}')
 
    #remove the game id 
    string = string[string.find(':'):]
    string = string[2:]
    ##split the games up
    game = string.split(";")
    print(game)
    highest_red = 0
    highest_green = 0
    highest_blue = 0
    for turn in game: 
    
        #split games up into turns 
        turn = turn.split(",")
        for roll in turn: 
        
            if 'red' in roll:
                redcount = re.sub('\D', '', roll)
                redcount = int(redcount)
                if redcount > highest_red:
                    highest_red = redcount
                    #return False
            if 'blue' in roll:
                bluecount = re.sub('\D', '', roll)
                bluecount = int(bluecount)
                if bluecount > highest_blue:
                    highest_blue = bluecount
                    #return False
            if 'green' in roll:
                greencount = re.sub('\D', '', roll)
                greencount = int(greencount)
                if greencount >highest_green:
                    highest_green = greencount
                       
                    #return False 
    power = highest_red * highest_green * highest_blue
    return power
    
for string in strings:
    i+=1
    sum = sum + int(check_strings(string))
    
print(sum)