def parse_input(path):
    result = []
    input = open(path, 'r')
    for line in input:
        result.append(list(line.split('\n')[0]))
    return result

def get_start_index(diagram):
    i = 0
    for item in diagram[0]:
        if item == 'S':
            return i
        else:
            i += 1

def process_beam(diagram, beam_index):
    resulting_beam_indices = []
    splits = 0

    if diagram[beam_index[1] + 1][beam_index[0]] == ".":
        resulting_beam_indices.append([beam_index[0], beam_index[1] + 1])
    elif diagram[beam_index[1] + 1][beam_index[0]] == "^":
        resulting_beam_indices.append([beam_index[0] - 1, beam_index[1] + 1])
        resulting_beam_indices.append([beam_index[0] + 1, beam_index[1] + 1])
        splits += 1
    
    return resulting_beam_indices, splits

def main():
    diagram = parse_input("2025\Day 7\input.txt")
    start_index = get_start_index(diagram)

    tachyon_beams = [[start_index, 0]]  # [x, y]
    end_reached = False
    split_count = 0

    while not end_reached:
        next_beam_round = []
        for beam_index in tachyon_beams:
            try:
                resulting_beam_indices, splits = process_beam(diagram, beam_index)
                split_count += splits
                for result in resulting_beam_indices:
                    if result not in next_beam_round:
                        next_beam_round.append(result)
            except:
                end_reached = True
        tachyon_beams = next_beam_round

    print(split_count)

main()