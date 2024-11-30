def main(lines):
    total_score = 0
    for line in lines:
       
        compartment_size = int(len(line) / 2)
       
        first_half = line[:compartment_size]
        second_half = line[compartment_size:]
        
        matching_char = check_for_match(first_half,second_half)
        if matching_char.isupper():
            total_score += ord(matching_char) - 38
        else:         
            total_score += ord(matching_char) -96

    print(total_score)

def check_for_match(first_half,second_half):
    for char_1 in list(first_half):
            for char_2 in list(second_half):
                if char_1 == char_2:
                
                    return char_1
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    main(lines)