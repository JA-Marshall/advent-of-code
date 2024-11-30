def main(lines):

    score_map = {
        #A ROCK 1 X LOSE 1
        #B PAPER 2 Y DRAW 3
        #C SCISSORS 3 Z WIN 6
        'A' : {'X' : 3, 'Y': 4,'Z': 8},
        'B' : {'X' : 1, 'Y': 5,'Z': 9},
        'C' : {'X' : 2, 'Y': 6, 'Z' : 7}
    }
    total_score = 0
    for line in lines:
        line = line.split(' ')
        total_score += score_map[line[0]][line[1]]
    
    print(total_score)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    main(lines)