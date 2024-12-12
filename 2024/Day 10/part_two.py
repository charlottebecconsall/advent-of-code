def parse_input():
    input = open("Day 10\input.txt", "r")
    input = input.read()
    input = input.split("\n")
    map = []
    trailheads = []
    for y in range(0, len(input)):
        line = input[y]
        mapped_line = []
        for x in range(0, len(line)):
            item = int(line[x])
            mapped_line.append(item)
            if item == 0:
                trailheads.append([x, y])
        map.append(mapped_line)
    return map, trailheads

def check_surrounding_squares(map, current_position):
    valid_next_steps = []
    x = current_position[0]
    y = current_position[1]
    level = map[y][x]
    try:
        if map[y+1][x] == (level+1):
            valid_next_steps.append([x, y+1])
    except IndexError as e:
        print("reached edge")

    try:
        if map[y][x+1] == (level+1):
            valid_next_steps.append([x+1, y])
    except IndexError as e:
        print("reached edge")
    

    if map[y-1][x] == (level+1) and (y-1) >= 0:
        valid_next_steps.append([x, y-1])
    if map[y][x-1] == (level+1) and (x-1) >= 0:
        valid_next_steps.append([x-1, y])
    
    return valid_next_steps


def find_paths(map, trailhead_index):
    valid_end_points = []
    x = trailhead_index[0]
    y = trailhead_index[1]
    valid_next_steps = check_surrounding_squares(map, [x, y])
    for step in valid_next_steps:
        if map[step[1]][step[0]] == 9:
            valid_end_points.append(step)
        else:
            for end_point in find_paths(map, step):
                valid_end_points.append(end_point)

    return valid_end_points

def main():
    map, trailheads = parse_input()
    result = 0
    for trailhead in trailheads:
        valid_end_points = find_paths(map, trailhead)
        result += len(valid_end_points)
    print(result)
    

main()