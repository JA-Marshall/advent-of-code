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
    for turn in game: 
    
        #split games up into turns 
        turn = turn.split(",")
        print(turn)
        for roll in turn: 
            print(roll)
        
            if 'red' in roll:
                redcount = re.sub('\D', '', roll)
                if int(redcount) > 12:
                      
                    print("too many reds!")
                    return False
            if 'blue' in roll:
                bluecount = re.sub('\D', '', roll)
                if int(bluecount) > 14:
                     
                    print("too many blues!")
                    return False
            if 'green' in roll:
                greencount = re.sub('\D', '', roll)
                if int(greencount) > 13:
                    print("too many greens!")
                       
                    return False 
    return True
    
for string in strings:
    i+=1
    if check_strings(string):
        sum = sum + i
        print(sum)
        
    else:
        pass
        #sum = sum + i
    #print(sum)
print(sum)