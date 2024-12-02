def parse_input(path):
    list_one = []
    list_two = []
    input = open(path, 'r')
    for line in input:
        line = line.split()
        list_one.append(int(line[0]))
        list_two.append(int(line[1]))
    return list_one, list_two

def main():
    list_one, list_two = parse_input("Day 1\input.txt")
    similarity_score_sum = 0
    for i in range(0, len(list_one)):
        multiplier = list_two.count(list_one[i])
        similarity_score = list_one[i] * multiplier
        similarity_score_sum += similarity_score
    print(similarity_score_sum)


main()