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
    return file_system

def reorder_file_system(file_system):
    end_index = len(file_system) - 1
    for i in range(0, len(file_system)):
        if file_system[i] == ".":
            while file_system[end_index] == "." and end_index > i:
                end_index -= 1
            file_system[i] = file_system[end_index]
            file_system[end_index] = "."
    return file_system

def calculate_checksum(file_system):
    checksum = 0
    for i in range(0, len(file_system)):
        if file_system[i] != ".":
            checksum += file_system[i] * i
    return checksum

def main():
    file_system = parse_input()
    reordered_file_system = reorder_file_system(file_system)
    checksum = calculate_checksum(reordered_file_system)
    print(checksum)


main()