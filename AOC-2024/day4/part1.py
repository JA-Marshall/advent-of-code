score = 0

def main(board):
    
  
    for row,string in enumerate(board):
    
        for col,char in enumerate(string):
            if char == 'X':
                check_direction(board,row,col)
    print(score) 
    
def check_direction(board,row,col):
    #left col + 1
    #up row + 1
    #right col -1
    #down row - 1
    # up_left  row -1 col -1
    # down_left  row +1 col -1
    # up_right = row -1 col +1
    # down_right = row +1 col +1

    if board[row][col + 1] == 'M':
        check_for_word(board,row,col,direction='left')
    if board[row +1][col] ==  'M':
        check_for_word(board,row,col,direction='up')
    if board[row][col -1] == 'M':
        check_for_word(board,row,col,direction='right')
    if board[row-1][col] == 'M':
        check_for_word(board,row,col,direction='down')
    if board[row-1][col-1] == 'M':
        check_for_word(board,row,col,direction= 'up_left')
    if board[row+1][col-1] == 'M':
        check_for_word(board,row,col,direction='down_left')
    if board[row-1][col+1] == 'M':
        check_for_word(board,row,col,direction='up_right')
    if board[row+1][col+1] == 'M':
        check_for_word(board,row,col,direction='down_right')

    pass

def check_for_word(board,row,col,direction):
    dir_map ={
    'left' : (0,1),
    'up' : (1,0),
    'right' : (0,-1),
    'down' : (-1,-0), 
    'up_left' : (-1,-1),
    'down_left' : (1,-1),
    'up_right' : (-1,1),
    'down_right' : (1,1)}
    
    row_mod,col_mod = dir_map[direction][0] * 2, dir_map[direction][1] * 2
    if board[row + row_mod][col + col_mod] == 'A':
        row_mod,col_mod = dir_map[direction][0] * 3, dir_map[direction][1] * 3
        if board[row + row_mod][col + col_mod] == 'S':
            add_score()

def add_score():
    global score
    score += 1
            

def generate_game_with_padding(lines):
    top_bottom = '_' * 140
    left_right = '_' * 3
    for i in range(3):
        lines.insert(0,top_bottom)
        lines.append(top_bottom)
    
    board = [list(f'{left_right}{line}{left_right}') for line in lines]
    
    return board
    


if __name__ == '__main__':
    with open('input.txt', 'r') as f:  
        lines = f.read().splitlines()
    board = generate_game_with_padding(lines)
    main(board)