def parse_input(path):
    result = []
    input = open(path, 'r')
    for line in input:
        result.append(line.split('\n')[0])
    return result

def rotate_dial(dial, existing_position, instruction):
    clicks = int(instruction[1:])
    direction = 1
    if instruction[0] == "L":
        direction = -1
    rotation = existing_position + (clicks * direction)
    num_loops = int(rotation / 100)
    rotation -= (100 * num_loops)
    new_position = dial[rotation]
    return new_position

def main():
    input = parse_input("2025\Day 1\input.txt")
    dial = [x for x in range(100)]
    current_position = 50
    counter = 0
    for instruction in input:
        current_position = rotate_dial(dial, current_position, instruction)
        if current_position == 0:
            counter += 1
    print(counter)

main()