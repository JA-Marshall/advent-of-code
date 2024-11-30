def main(lines):

    score_map = {
        'X' : {'A' : 4, 'B': 5,'C': 7},
        'Y' : {'A' : 8, 'B': 5,'C': 2},
        'Z' : {'A' : 3, 'B': 9, 'C' : 6}
    }
    total_score = 0
    for line in lines:
        line = line.split(' ')
        total_score += score_map[line[-1]][line[0]]
    
    print(total_score)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    main(lines)