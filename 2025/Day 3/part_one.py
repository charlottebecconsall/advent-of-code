def parse_input(path):
    result = []
    input = open(path, 'r')
    for line in input:
        result.append(line.split('\n')[0])
    return result


def find_max_joltage(battery_bank):
    max_joltage_bat_1 = 0
    max_joltage_bat_2 = 0
    bat_1_index = 0

    for i in range(len(battery_bank)-1):
        if int(battery_bank[i]) > int(max_joltage_bat_1):
            max_joltage_bat_1 = battery_bank[i]
            bat_1_index = i

    for j in range(bat_1_index+1, len(battery_bank)):
        if int(battery_bank[j]) > int(max_joltage_bat_2):
            max_joltage_bat_2 = battery_bank[j]
    
    max_joltage = str(max_joltage_bat_1) + str(max_joltage_bat_2)
    
    return int(max_joltage)


def main():
    battery_banks = parse_input("2025\Day 3\input.txt")
    total_output_joltage = 0
    for battery_bank in battery_banks:
        max_joltage = find_max_joltage(battery_bank)
        total_output_joltage += max_joltage
    print(total_output_joltage)

main()