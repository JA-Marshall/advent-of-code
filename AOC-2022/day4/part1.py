def main(lines):
    count = 0
    for line in lines:
        pair =line.split(',')
        print(pair)
        elf_1_start,elf_1_end = pair[0].split('-')
        elf_2_start,elf_2_end = pair[1].split('-')
        elf_1_start,elf_1_end,elf_2_start,elf_2_end = int(elf_1_start),int(elf_1_end),int(elf_2_start),int(elf_2_end)
        
        if elf_1_start >= elf_2_start and elf_1_end <= elf_2_end:
            count +=1 
            continue
        if elf_2_start >= elf_1_start and elf_2_end <= elf_1_end:
            count+=1            

        
    print(count)



if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    main(lines)