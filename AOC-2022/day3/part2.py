import numpy as np
from collections import Counter

def main(lines):
    total_score = 0
    matching_chars = []
    string_to_check = ''
    print(lines)
    while lines:
        

        line_1 = lines[0]
        line_2 = lines[1]
        line_3 = lines[2]

        matching_char = list((set(line_1) & set(line_2) & set(line_3)))

     
        
        if matching_char[0].isupper():
            total_score += ord(matching_char[0]) - 38
        else:         
            total_score += ord(matching_char[0]) -96
        lines =lines[3:]
    
    print(total_score)

# def check_for_match(first_half,second_half):
#     for char_1 in list(first_half):
#             for char_2 in list(second_half):
#                 if char_1 == char_2:
                
#                     return char_1
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    main(lines)