
score = 0

def main(board):
    
  
    for row,string in enumerate(board):
    
        for col,char in enumerate(string):
            if char == 'A':
                check_for_mas(board,row,col)
    print(score) 
    
def check_for_mas(board,row,col):
    
    # up_left  row -1 col -1
    # ()
    #    A    row -1 col + 1
    #---------------------
    #      ()   
    #    A       row - 1 col  +1 
    #-------------------------
    #    A
    # ()         row +1  col -1  
    #--------------------------
    #    A 
    #       ()    row + 1 col +1
    #

    # down_left  row +1 col -1
    # up_right = row -1 col +1
    # down_right = row +1 col +1

    if board[row -1][col-1] =='M':
        if board[row+1][col +1] == 'S':
            check_other_possible_mas(board,row,col)

    if board[row -1][col-1] =='S':
        if board[row+1][col +1] == 'M':
            check_other_possible_mas(board,row,col)
    
            
def check_other_possible_mas(board,row,col):
    if board[row-1][col +1] == 'M':
        if board[row+1][col -1] == 'S':
            add_score()
    elif board[row-1][col +1] == 'S':
        if board[row+1][col -1] == 'M':
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