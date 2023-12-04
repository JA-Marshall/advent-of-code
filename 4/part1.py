

def main(strings):
    #multiplier_tracker = {}
    score = 0 
    i = 0
    for string in strings:
        card = string.split(':')
        card = card[1]
        scorecard = card.split('|')
        #print(scorecard)
        winning_numbers = scorecard[0].split()
        print(winning_numbers)
        numbers_to_check = scorecard[1].split()
        print(numbers_to_check)
        matches = []
        for number in numbers_to_check:
            if number in winning_numbers:
                matches.append(number)
        
        if len(matches) > 0:
            gamescore = 1 
            for i in range(len(matches) - 1): 
                gamescore = gamescore * 2 
            score = score + gamescore
    return score





if __name__=="__main__":
    file = open("list.txt","r")
    data = file.readlines()
    strings = []

    for line in data:
        strings.append(line.replace("\n",""))
    print(main(strings))
    
    
