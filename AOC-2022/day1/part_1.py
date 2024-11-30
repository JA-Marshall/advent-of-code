def main(lines):
    totals = []
    deer_total = 0
    for line in lines:
        if line == '':
            totals.append(deer_total)
            deer_total = 0
        else:
            deer_total = deer_total + int(line)
    print(max(totals))


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    main(lines)