def parse_input(path):
    result = []
    input = open(path, 'r')
    for line in input:
        result.append(line.split('\n')[0])
    return result


def find_max_joltage(battery_bank):
    max_joltage = ""
    test_max_joltage = 0
    bat_index = -1
    num_bats_left_to_turn_on = 12

    while num_bats_left_to_turn_on > 0:
        for i in range(bat_index+1, len(battery_bank)-num_bats_left_to_turn_on+1):
            if int(battery_bank[i]) > int(test_max_joltage):
                test_max_joltage = battery_bank[i]
                bat_index = i
        num_bats_left_to_turn_on -= 1
        test_max_joltage = 0
        max_joltage = max_joltage + str(battery_bank[bat_index])
    
    return int(max_joltage)


def main():
    battery_banks = parse_input("2025\Day 3\input.txt")
    total_output_joltage = 0
    for battery_bank in battery_banks:
        max_joltage = find_max_joltage(battery_bank)
        total_output_joltage += max_joltage
    print(total_output_joltage)

main()