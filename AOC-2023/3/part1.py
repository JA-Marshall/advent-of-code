import re

def populate_symbol_adjacency_board(strings):
    #generates board and populates all areas adjacent or including a symbol with 1

    board = [[0 for _ in range(140)] for _ in range (140)]

    for y_idx, string in enumerate(strings):
        for x_idx, char in enumerate(string):
            if char != '.' and not char.isdigit():
                board[y_idx+1][x_idx] = 1 # Down
                board[y_idx-1][x_idx] = 1 # Up
                board[y_idx][x_idx+1] = 1 # Right
                board[y_idx][x_idx-1] = 1 # Left
                board[y_idx+1][x_idx+1] = 1 # Down Right
                board[y_idx+1][x_idx-1] = 1 # Down Left
                board[y_idx-1][x_idx+1] = 1 # Up Right
                board[y_idx-1][x_idx-1] = 1 # Down Right

    return board


def check_board(board, strings):
    #check if any positions that contain a number 

    sum = 0 
    for y_idx, string in enumerate(strings):
        for match in re.finditer(r"\b\d+\b", string):
            start_coord = match.start()
            end_coord = match.end()
            number = match.group()
            if (1 in board[y_idx][start_coord:end_coord]):
                sum += int(number)
    
    return sum

if __name__=="__main__":
    file = open("list.txt","r")
    data = file.readlines()
    strings = []

    for line in data:
        strings.append(line.replace("\n",""))

    board = populate_symbol_adjacency_board(strings)

    print(check_board(board, strings))