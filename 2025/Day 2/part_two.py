def parse_input(path):
    result = []
    input = open(path, 'r')
    for line in input:
        result = line.split(',')
    return result

def check_id_valid(id):
    id = str(id)
    result = True

    for i in range(1, int(len(id)/2)+1):
        if len(id) % i == 0:
            test_pattern = id[0:i]
            x = i
            for j in range(i*2, len(id)+1, i):
                check_pattern = id[x:j] 
                x += i
                if test_pattern != check_pattern:
                    break
            else:
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