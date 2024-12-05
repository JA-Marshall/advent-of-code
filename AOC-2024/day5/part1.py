from collections import defaultdict

def main(lines):
    score = 0
    ordering_rules = defaultdict(list)
    for i,line in enumerate(lines):
        if line == '':
            lines = lines[i+1:]
            break

        r1,r2 = line.split('|')
        ordering_rules[r1].append(r2)

    page_orders = []
    for line in lines:
        rules = line.split(',')
        page_orders.append(rules)

    for page_order in page_orders:
        if check_if_valid_page_order(page_order,ordering_rules):
           
            middle_index = len(page_order)//2
            score += int(page_order[middle_index])

    print(score)

def check_if_valid_page_order(page_order,ordering_rules):
        
        for i,page in enumerate(page_order):
            next_pages = set(page_order[i+1:])
            must_be_before = set(ordering_rules[page])
            
            if not next_pages.issubset(must_be_before):
                return 0
        return True

if __name__ == '__main__':
    with open('input.txt', 'r') as f:  
        lines = f.read().splitlines()
 
    main(lines)