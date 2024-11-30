from dataclasses import dataclass

def main(lines):
    directory_tree = {'/' : {}}
    current_pwd= ''
    current_dir = ''
    for line in lines:
        if 'cd /' in line:
            current_pwd = ''
            current_dir = '/'
            print(line)
            
        elif 'cd ..' in line:

            current_pwd = current_pwd.replace(f'/{current_dir}','')
            
            print(line)

        elif 'cd ' in line:
            _,dir = line.split('cd ')
            print(dir)
            current_dir = f'{dir}'
            current_pwd = f'{current_pwd}/{dir}'
            print(line)
        
        if 'dir ' in line:
            print(line)
            _, child_name = line.split(' ')
            

        print(current_pwd)
        print(current_dir)
    
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    main(lines)