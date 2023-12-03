import re 

def main(lists_of_characterlists):
    for x, row in enumerate(lists_of_characterlists):
        for y, char in enumerate(row):
            if char == '*':
                print("found a *")
                abovestring = extract_area_as_string(lists_of_characterlists,x-1,y,7,1)
                middlestring = extract_area_as_string(lists_of_characterlists,x,y,7,1)
                belowstring = extract_area_as_string(lists_of_characterlists,x+1,y,7,1)
                print(abovestring)
                print(middlestring)
                print(belowstring)


               

                
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
    
    


