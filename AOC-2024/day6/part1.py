from itertools import cycle
score = 0
def main(board):
    for row,string in enumerate(board):
        for col,char in enumerate(string):
            if char == '^':
                final_board = start_pathing(board,starting_row=row,starting_col=col)
                count_positions(final_board)
            
def start_pathing(board,starting_row,starting_col):
    print(starting_row, starting_col)
    facing = cycle([[-1,0],[0,1],[1,0],[0,-1]])
    current_direction = get_next_direction(facing)
    g_row,g_col = starting_row + current_direction[0], starting_col + current_direction[1]
    board[g_row][g_col] = 'X'
    
   
    while True:
        g_row,g_col = g_row+ current_direction[0], g_col + current_direction[1]
    
        next_row,next_col = g_row + current_direction[0], g_col + current_direction[1]
        if next_row < 0 or next_row >= len(board):
            print("OOB")
            board[g_row][g_col] = 'X'
            return board
        if next_col < 0 or next_col >= len(board[next_row]):
            print("OOB")
            board[g_row][g_col] = 'X'
            return board
      
        if board[next_row][next_col] == '#':
            current_direction = get_next_direction(facing)
        board[g_row][g_col] = 'X'

        print(g_row,g_col)

def get_next_direction(facing):
    return next(facing)
    
def count_positions(board):
    count = 0
    for row,string in enumerate(board):
        for col,char in enumerate(string):
            if char == 'X' or char == '^':
                count+=1
 
    print(count)


    
if __name__ == '__main__':
    with open('input.txt', 'r') as f:  
        lines = f.read().splitlines()
    board = [list(line) for line in lines]
 
    main(board)