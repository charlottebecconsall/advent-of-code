def parse_input(input):
    rules_dict = {}
    updates = []
    for line in input:
        line = line.strip("\n")
        if '|' in line:
            line = line.split("|")
            if line[0] in rules_dict.keys():
                rules_dict[line[0]] = rules_dict[line[0]] + "," + line[1]
            else:
                rules_dict[line[0]] = line[1]
        elif ',' in line:
            line = line.split(",")
            updates.append(line)
    return rules_dict, updates


def check_update_is_correct(rules_dict, update):
    is_correct = True
    index = 0
    for num in update:
        if num in rules_dict.keys():
            relevant_rule = rules_dict[num]
            comes_before = relevant_rule.split(",")
            for i in range(index, -1, -1):
                if update[i] in comes_before:
                    is_correct = False
        index += 1
    return is_correct


def get_middle_num(update):
    middle_num = int(update[int(len(update)/2)])
    return middle_num


def main():
    input = open("Day 5\input.txt", 'r')
    rules_dict, updates = parse_input(input)
    result = 0
    for update in updates:
        if check_update_is_correct(rules_dict, update):
            middle_num = get_middle_num(update)
            result += middle_num
    print(result)


main()
