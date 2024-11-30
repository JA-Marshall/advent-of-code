def main(line):
    
    chars = list(line[0])
   
    buffer = chars[:4]
    
    for i in range(len(chars)):
        buffer.pop(0)
        buffer.append(chars.pop(0))
        print(buffer)
        if len(set(buffer)) == 4:
            print(i +1)
            break

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        line = f.read().splitlines()
    main(line)
