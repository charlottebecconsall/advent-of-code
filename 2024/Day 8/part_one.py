def parse_input():
    input = open("Day 8/input.txt", "r")
    mapped_area = []
    for line in input:
        mapped_area.append(list(line.strip("\n")))
    return mapped_area

def get_unique_signals(mapped_area):
    unique_signals = {}
    for y in range(0, len(mapped_area)):
        for x in range(0, len(mapped_area[0])):
            if mapped_area[y][x] not in unique_signals.keys() and mapped_area[y][x] != ".":
                unique_signals[mapped_area[y][x]] = [[x, y]]
            elif mapped_area[y][x] != ".":
                unique_signals[mapped_area[y][x]].append([x, y])
    return unique_signals

def check_antinode_in_bounds(antinode, mapped_area):
    in_bounds = True
    if antinode[0] >= len(mapped_area[0]) or antinode[0] < 0:
        in_bounds = False
    if antinode[1] >= len(mapped_area) or antinode[1] < 0:
        in_bounds = False
    return in_bounds


def get_antinodes(signal, unique_signals, mapped_area):
    antinodes = []
    for i in range(0, len(unique_signals) - 1):
        for j in range(i+1, len(unique_signals)):
            pos_1 = unique_signals[i]
            pos_2 = unique_signals[j]
            antinode_diff = (pos_1[0] - pos_2[0], pos_1[1] - pos_2[1])
            antinode_1 = [pos_1[0] + antinode_diff[0], pos_1[1] + antinode_diff[1]]
            antinode_2 = [pos_2[0] - antinode_diff[0], pos_2[1] - antinode_diff[1]]
            if check_antinode_in_bounds(antinode_1, mapped_area):
                antinodes.append(antinode_1)
            if check_antinode_in_bounds(antinode_2, mapped_area):
                antinodes.append(antinode_2)

    return antinodes


def main():
    mapped_area = parse_input()
    unique_signals = get_unique_signals(mapped_area)
    antinodes = []
    for signal in unique_signals.keys():
        antinode_positions = get_antinodes(signal, unique_signals[signal], mapped_area)
        for antinode in antinode_positions:
            if antinode not in antinodes:
                antinodes.append(antinode)
    print(len(antinodes))


main()
