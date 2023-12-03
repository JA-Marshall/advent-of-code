import re 

def main(lists_of_characterlists):

    
    for x, row in enumerate(lists_of_characterlists):
        for y, char in enumerate(row):
            if char == '*':
                print("found a *")
                top = [0,1]
                topleft = [-1,1]
                topright = [1,1]
                middeleft = [-1,0]
                middleright = [1,0]
                bottomleft = [-1,-1]
                bottommiddle = [0,-1]
                bottomright = [1,-1]

                topleftnum = check_backwards(lists_of_characterlists,topleft)
                print(topleftnum)
             

def check_backwards(lists_of_characterlists,starting_offset):
    number = ''
    i = 0
    while lists_of_characterlists[(starting_offset[0])-i][starting_offset[1]].isdigit():
        number = number + lists_of_characterlists[(starting_offset[0])-i][starting_offset[1]]
        i+=1
    number = number[::-1]
    return number


               

                




if __name__=="__main__":
    file = open("list.txt","r")
    data = file.readlines()
    strings = []

    for line in data:
        strings.append(line.replace("\n",""))
    lists_of_characterlists = [list(string) for string in strings]
    main(lists_of_characterlists)
    
    


