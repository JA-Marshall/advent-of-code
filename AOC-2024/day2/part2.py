def main(lines):
    score = 0
    for line in lines: 
        numbers = [int(x) for x in line.split()]
        
        for i,n in enumerate(numbers):
            nums2 = numbers.copy()

            nums2.pop(i)
            if is_safe(nums2):
                score+=1
                break
                
    print(score)
def is_safe(numbers):

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

        if line_safe:
            return True

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    main(lines)
    