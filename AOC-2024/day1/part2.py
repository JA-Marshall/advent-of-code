from collections import Counter
import time 

def main(lines):
    first_numbers = []
    second_numbers = []
    total_score= 0
    
    for line in lines: 
        n1,n2 = line.split('   ')
        n1,n2 = int(n1),int(n2)
        first_numbers.append(n1)
        second_numbers.append(n2)

    second_counts = Counter(second_numbers)

    for number in first_numbers:   
        total_score += second_counts[number] * number
    
    print(total_score)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()      
    main(lines)
    
    
