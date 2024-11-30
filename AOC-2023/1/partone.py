from collections import deque

file = open("list.txt","r")
data = file.readlines()
strings = []
for line in data:
    strings.append(line.replace("\n",""))

calibration_codes = []


    
    
def get_first_int(chars):
    while True:
   
        char = chars[0]
        if char.isdigit(): 
            return char
        
        else: 
        
            chars.pop(0)

print(strings)
value = 0
for string in strings: 
    chars = [*string]
    first_digit = get_first_int(chars)
    chars.reverse()
    second_digit=(get_first_int(chars))
    digits = f'{first_digit}{second_digit}'
    value = value + int(digits)

print(value)