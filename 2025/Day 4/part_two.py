def parse_input(path):
    result = []
    input = open(path, 'r')
    for line in input:
        line = line.split('\n')[0]
        result.append(line)
    return result

def pad_map(map):
    new_map = [list("."*(len(map[0])+2))]
    for line in map:
        new_map.append(list("." + line + "."))
    new_map.append(list("."*(len(map[0])+2)))
    return new_map

def check_adjacent_positions(map, location_x, location_y):
    adjacent_rolls = 0

    # check right
    try:
        if map[location_y][location_x + 1] == "@":
            adjacent_rolls += 1
    except:
        pass
    # check left
    try:
        if map[location_y][location_x - 1] == "@":
            adjacent_rolls += 1
    except:
        pass
    # check up
    try:
        if map[location_y - 1][location_x] == "@":
            adjacent_rolls += 1
    except:
        pass
    # check down
    try:
        if map[location_y + 1][location_x] == "@":
            adjacent_rolls += 1
    except:
        pass
    # check left up diagonal
    try:
        if map[location_y - 1][location_x - 1] == "@":
            adjacent_rolls += 1
    except:
        pass
    # check right up diagonal
    try:
        if map[location_y - 1][location_x + 1] == "@":
            adjacent_rolls += 1
    except:
        pass
    # check left down diagonal
    try:
        if map[location_y + 1][location_x - 1] == "@":
            adjacent_rolls += 1
    except:
        pass
    # check right down diagonal
    try:
        if map[location_y + 1][location_x + 1] == "@":
            adjacent_rolls += 1
    except:
        pass

    return adjacent_rolls
    

def main():
    map = parse_input("2025\Day 4\input.txt")
    map = pad_map(map)
    rolls_removed = 0
    rolls_removed_this_round = -1
    
    while rolls_removed_this_round != 0:
        rolls_removed_this_round = 0
        for y in range(1, len(map)-1):
            for x in range(1, len(map[0])-1):
                if map[y][x] == "@":
                    num_adjacent_rolls = check_adjacent_positions(map, x, y)
                    if num_adjacent_rolls < 4:
                        rolls_removed_this_round += 1
                        map[y][x] = "."
        rolls_removed += rolls_removed_this_round

    print(rolls_removed)

main()