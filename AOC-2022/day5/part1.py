import pprint
def main(lines):
    crate_lines = []
    move_list = []
    game_dict = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}

    for index,line in enumerate(lines):
        if 'move' in line:
            
            move_list = lines[index:]
            crate_lines = lines[:index]
            
           
            break
    
    for line in crate_lines:
        if '1' in line:
            break
        
        for i in range(9):
            char = (line[(i * 4) + 1])
            
            if char.isalpha():
                game_dict[i+1].append(char)

    for move in move_list:
        number_to_move, to_be_moved = move.split(' from ')
        
        _,number_to_move = number_to_move.split(' ') 
    
        move_from, move_to = to_be_moved.split(' to ')
        
    
        for i in range(int(number_to_move)):
            block = game_dict[int(move_from)].pop(0)
            game_dict[int(move_to)].insert(0,block)
    pprint.pp(game_dict)
    final_string = ''
    for i in range(9):
        final_string += game_dict[i + 1].pop(0)
        
      
    print(final_string)
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    main(lines)
