def main(lines):
    total = 0
    # lines = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
    do_flag = ['d','o','(',')']
    dont_flag = ['d','o','n',"'"]
    target = ['m','u','l','(']
    do_enabled = True
    for line in lines:
        chars = list(line)
        buffer = chars[:4]
        
        for i in range(len(line)):
            # print(buffer)
            if buffer == do_flag:
                do_enabled = True
            if buffer == dont_flag:
                do_enabled = False
           
            if buffer == target and do_enabled:
                total += parse_match(line[i:i+8])   
               
            if chars:         
                buffer.pop(0)
                buffer.append(chars.pop(0))
    
    print(total)

def parse_match(numbers_after_mul):
         
    num1,num2 ='',''      
    num1_complete = False
    print(numbers_after_mul)

    for char in numbers_after_mul:
        
        if ')' not in numbers_after_mul:   
            return 0
        
        if char == ',':           
            num1_complete = True

        elif char.isdigit() and num1_complete == False:
            num1+= char

        elif char.isdigit() and num1_complete:
            num2+= char

    if num1 and num2:
        num1,num2 = int(num1),int(num2)
    
        return num1 * num2
    return 0
    
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    main(lines)
    