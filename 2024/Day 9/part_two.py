def parse_input():
    input = open("Day 9\input.txt", "r")
    input = input.read()
    file_system = []
    i = 0
    file_id = 0
    for num in input:
        if i % 2 == 0:
            for j in range(0, int(num)):
                file_system.append(file_id)
            file_id += 1
        else:
            for j in range(0, int(num)):
                file_system.append(".")
        i += 1
    max_id = file_id - 1
    return file_system, max_id

def find_space(file_system, space_required, id):
    space_found = False
    max_reached = False
    start_index = file_system.index(".") # gets index of first instance of empty space
    stop_index = start_index
    max_index = file_system.index(id)
    while not space_found and not max_reached:
        if stop_index <= max_index:
            if stop_index - start_index >= space_required:
                space_found = True

            if file_system[stop_index] == ".":
                stop_index += 1
            elif not space_found:
                start_index = stop_index + 1
                stop_index = start_index
        else:
            max_reached = True
    if space_found:
        stop_index = start_index + space_required
    return space_found, start_index, stop_index

def reorder_file_system(file_system, max_id):
    for id in range(max_id, -1, -1):
        space_required = file_system.count(id)
        space_found, start_index, stop_index = find_space(file_system, space_required, id)
        if space_found:
            file_system[start_index:stop_index] = [id] * space_required
            for i in range(len(file_system)-1, (stop_index-1), -1):
                if file_system[i] == id:
                    file_system[i] = "."
    return file_system

def calculate_checksum(file_system):
    checksum = 0
    for i in range(0, len(file_system)):
        if file_system[i] != ".":
            checksum += file_system[i] * i
    return checksum

def main():
    file_system, max_id = parse_input()
    reordered_file_system = reorder_file_system(file_system, max_id)
    print(reordered_file_system)
    checksum = calculate_checksum(reordered_file_system)
    print(checksum)

def test():
    test_system = [".",".",0,0]
    test_system= reorder_file_system(test_system, 0)
    print(test_system)


main()
# test()