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
        chars = chars[4:]
        line = list(line)
        
        for i in range(len(line)):
            print(buffer)
            if buffer == do_flag:
                do_enabled = True
            if buffer == dont_flag:
                do_enabled = False
           
            if buffer == target and do_enabled:
                
                numbers_after_mul = line[i+4:i+12]          
                num1,num2 ='',''      
                final_num1 = False
                
                for i,value in enumerate(numbers_after_mul):
                    
                    if value == ',':
                      
                        final_num1 = True

                    elif value.isdigit() and final_num1:
                        num2+= value

                    elif value.isdigit() and final_num1 == False:
            
                        num1+= value
                    if ')' not in numbers_after_mul:
                        num1, num2 = '',''
                         
                if num1 and num2:
                    num1,num2 = int(num1),int(num2)
                    total_to_add = num1 * num2
                    print(f'{num1} {num2}')
                    total += total_to_add
                    
            if len(chars) > 0:         
                buffer.pop(0)
                buffer.append(chars.pop(0))
    
    print(total)

    
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    main(lines)
    