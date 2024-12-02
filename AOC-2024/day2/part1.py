def main(lines):
    score = 0
    for line in lines: 
        numbers = [int(x) for x in line.split()]
        print(numbers)
        line_safe = False
    
            
        if sorted(numbers) == numbers or sorted(numbers,reverse=True) == numbers:
            line_safe = True 
            print("sorted")
        n1 = numbers[0]
        for i, n1 in enumerate(numbers[:-1]):
            n2 = numbers[i + 1]
            diff = abs(n2-n1)
            
            if diff >3 or diff <1:
               line_safe = False

        print(line_safe)

        if line_safe: 
            score +=1
    print(score)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    main(lines)
    