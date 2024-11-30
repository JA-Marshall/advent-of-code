import numpy as np

file = open("list.txt","r")
data = file.readlines()
strings = []
for line in data:
    strings.append(line.replace("\n",""))

calibration_codes = []



def get_num_from_string(string):
    
    numberlist = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    lowest_instance =999999999
    first_digits = ['none']
    highest_instance = 0
    second_digits = ['none']
    final_first = 0
    final_second = 0
    print(string)
    for number in numberlist:
        first_instance = string.find(number)
        #print(first_instance)
        chars = [*string]
        
        if first_instance != -1:
            if first_instance < lowest_instance:
                lowest_instance = first_instance
                
                
                first_digits[0] = number

        last_instance = string.rfind(number)
        if last_instance != -1:
            if last_instance > highest_instance:
                highest_instance = last_instance
                second_digits[0] = number
        
   
  
    first_digits.append( get_first_int(chars))
    chars.reverse()
    second_digits.append(get_first_int(chars))
   
    firstintindex = string.find(first_digits[1])
    
    secondintindex = string.rfind(second_digits[1])
    print(f"Lowest : Highest str index {lowest_instance}   {highest_instance}")
    print(f"lowest:highst int index  {firstintindex}   {secondintindex}")
    if first_digits[0] == 'none':
        final_first = first_digits[1]
    
    if lowest_instance < firstintindex:
        final_first = numberlist.index(first_digits[0]) + 1
    else: 
        final_first = first_digits[1]
    if highest_instance > secondintindex:
        final_second = numberlist.index(second_digits[0]) + 1
    else:
        final_second = second_digits[1]
    value = f'{final_first}{final_second}'
    

    return int(value)



def get_first_int(chars):
    while True:
   
        char = chars[0]
        if char.isdigit(): 
            return char
        
        else: 
        
            chars.pop(0)

value = 0

for string in strings:
    #value = value + int(get_num_from_string(string))
    value = value + get_num_from_string(string)
    
print(value)