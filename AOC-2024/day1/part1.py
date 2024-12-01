

def main(lines):
    first_numbers = []
    second_numbers = []
    total_distance = 0
    for line in lines: 
        n1,n2 = line.split('   ')
        n1,n2 = int(n1),int(n2)
        first_numbers.append(n1)
        second_numbers.append(n2)
    print(first_numbers)
    first_numbers.sort()
    second_numbers.sort()
    
    for i in range(len(lines)):
        distance = abs(first_numbers[i] - second_numbers[i])
        total_distance += distance

    print(total_distance)
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    main(lines)
    
