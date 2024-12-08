def parse_input():
    input = open("Day 6/input.txt", "r")
    mapped_area = []
    for line in input:
        mapped_area.append(list(line.strip("\n")))
    return mapped_area

def find_guard(mapped_area):
    y = 0
    guard_position = [0, 0]
    for row in mapped_area:
        x = 0
        for item in row:
            if item == "^":
                guard_position[0] = x
                guard_position[1] = y   # is this pass by ref or val? can't remember oop
            x += 1
        y += 1
    return guard_position

def change_guard(guard):
    if guard == "^":
        new_guard = ">"
    if guard == ">":
        new_guard = "v"
    if guard == "v":
        new_guard = "<"
    if guard == "<":
        new_guard = "^"
    return new_guard

def check_direction(guard):
    # Provide a start stop step list for passing into further things
    if guard == "^":
        direction = [0, -1] # -1 y each time, 0 x change
    if guard == ">":
        direction = [1, 0]
    if guard == "v":
        direction = [0, 1]
    if guard == "<":
        direction = [-1, 0]
    return direction

def find_guard_path(mapped_area, guard_position):
    guard = mapped_area[guard_position[1]][guard_position[0]]
    direction = check_direction(guard)
    exit_found = False
    x = guard_position[0]
    y = guard_position[1]
    while not exit_found:
        try:
            next_y = y + direction[1]
            next_x = x + direction[0]
            if next_x >= 0 and next_y >= 0:
                if mapped_area[next_y][next_x] == "#":
                    guard = change_guard(guard)
                    direction = check_direction(guard)
                    mapped_area[y][x] = guard
                else:
                    mapped_area[y][x] = "X"
                    x += direction[0]
                    y += direction[1]
            else:
                mapped_area[y][x] = "X"
                exit_found = True
        except:
            mapped_area[y][x] = "X"
            exit_found = True
    return mapped_area


def count_guard_positions(mapped_area):
    count = 0
    for row in mapped_area:
        for item in row:
            if item == "X":
                count += 1
    return count


def main():
    mapped_area = parse_input()
    guard_position = find_guard(mapped_area)
    mapped_area = find_guard_path(mapped_area, guard_position)
    count = count_guard_positions(mapped_area)
    print(count)

main()