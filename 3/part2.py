import re 

def main(lists_of_characterlists):

    
    for x, row in enumerate(lists_of_characterlists):
        for y, char in enumerate(row):
            if char == '*':
                print("found a *")
                positions = {
                    'top': (0,1),
                    'topleft': (-1,1),
                    'topright': (1,1),
                    'middleleft': (-1,0),
                    'middleright': (1,0),
                    'bottomleft': (-1,-1),
                    'bottommiddle': (0,-1),
                    'bottomright': (1,-1)
                }

                ###debug code for printing area around the * 
                abovestring = extract_area_as_string(lists_of_characterlists,x-1,y,7,1)
                middlestring = extract_area_as_string(lists_of_characterlists,x,y,7,1)
                belowstring = extract_area_as_string(lists_of_characterlists,x+1,y,7,1)
                print(abovestring)
                print(middlestring)
                print(belowstring)


                for name, pos in positions.items():
                    start = (x + pos[0], y + pos[1])
                    print(f'From {name} position: {find_number_start(lists_of_characterlists, start)}')

def find_number_start(array, start):
    row, col = start
    number = ''
    while col >= 0:
        if not str(array[row][col]).isdigit():
            break
        number = str(array[row][col]) + number
        col -= 1
    return number
               
##debug code just to print out the area im working with 
def extract_area_as_string(array, x, y, width, height):
    row_offset = height // 2
    col_offset = width // 2

    start_row = max(0, x - row_offset)
    end_row = min(len(array), x + 1 + row_offset)

    start_col = max(0, y - col_offset)
    end_col = min(len(array[0]), y + 1 + col_offset)

    area_to_extract = [row[start_col:end_col] for row in array[start_row:end_row]]

    area_string = "\n".join([" ".join(map(str, row)) for row in area_to_extract])

    return area_string




if __name__=="__main__":
    file = open("list.txt","r")
    data = file.readlines()
    strings = []

    for line in data:
        strings.append(line.replace("\n",""))
    lists_of_characterlists = [list(string) for string in strings]
    main(lists_of_characterlists)
    
    


