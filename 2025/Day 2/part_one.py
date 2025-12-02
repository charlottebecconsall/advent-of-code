def parse_input(path):
    result = []
    input = open(path, 'r')
    for line in input:
        result = line.split(',')
    return result

def check_id_valid(id):
    id = str(id)
    result = True

    if len(id) % 2 == 0:
        test_pattern = id[0:len(id) // 2]
        check_pattern = id[len(id) // 2 :]
        if test_pattern == check_pattern:
            result = False

    return result

def find_invalid_ids(id_range):
    invalid_ids = []
    id_range_start = id_range.split('-')[0]
    id_range_stop = id_range.split('-')[1]
    for id in range(int(id_range_start),int(id_range_stop)+1):
        if not check_id_valid(id):
            invalid_ids.append(int(id))
    return invalid_ids

def main():
    input = parse_input("2025\Day 2\input.txt")
    result = 0
    for id_range in input:
        invalid_ids = find_invalid_ids(id_range)
        for invalid_id in invalid_ids:
            result += invalid_id
    print(result)

main()