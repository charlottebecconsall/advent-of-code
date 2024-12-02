
def parse_input(path):
    list_one = []
    list_two = []
    input = open(path, 'r')
    for line in input:
        line = line.split()
        list_one.append(line[0])
        list_two.append(line[1])
    return list_one, list_two

def main():
    list_one, list_two = parse_input("Day 1\input.txt")
    list_one.sort()
    list_two.sort()
    diff_sum = 0
    for i in range(0, len(list_one)):
        diff = abs(int(list_one[i]) - int(list_two[i]))
        diff_sum += diff
    print(diff_sum)


main()
