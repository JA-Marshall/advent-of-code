def main(line):
    print(len(line))
    print(len(line[0]))
    chars = list(line[0])
    buffer = chars[:14]
  
    for i in range(len(chars)):
        buffer.pop(0)
        buffer.append(chars.pop(0))
        # print(buffer)
        # print(len(set(buffer)))
     
        if len(set(buffer)) == 14:
            print(i +1)
            break
    
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        line = f.read().splitlines()
    main(line)
