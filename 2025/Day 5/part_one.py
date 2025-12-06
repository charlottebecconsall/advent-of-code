def parse_input(path):
    fresh_ranges = []
    available = []
    input = open(path, 'r')
    for line in input:
        if "-" in line:
            fresh_ranges.append(line.split('\n')[0])
        elif line != '\n':
            available.append(line.split('\n')[0])
    return fresh_ranges, available


def check_freshness(fresh_ranges, ingredient_id):
    fresh = 0
    for fresh_range in fresh_ranges:
        range_start = int(fresh_range.split('-')[0])
        range_stop = int(fresh_range.split('-')[1])
        if int(ingredient_id) >= range_start and int(ingredient_id) <= range_stop:
            fresh = 1
            break
    return fresh


def main():
    fresh_ranges, available = parse_input("2025\Day 5\input.txt")
    fresh_counter = 0
    for ingredient_id in available:
        fresh_counter += check_freshness(fresh_ranges, ingredient_id)
    print(fresh_counter)

main()