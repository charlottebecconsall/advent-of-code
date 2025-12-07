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
    beam_index = beam_index.split(",")
    beam_index = [int(i) for i in beam_index]
    resulting_beam_indices = []
    splits = 0

    if diagram[beam_index[1] + 1][beam_index[0]] == ".":
        resulting_beam_indices.append([beam_index[0], beam_index[1] + 1])
    elif diagram[beam_index[1] + 1][beam_index[0]] == "^":
        resulting_beam_indices.append([beam_index[0] - 1, beam_index[1] + 1])
        resulting_beam_indices.append([beam_index[0] + 1, beam_index[1] + 1])
    
    return resulting_beam_indices

def main():
    diagram = parse_input("2025\Day 7\input.txt")
    start_index = get_start_index(diagram)

    tachyon_beams = {"{0}, 0".format(start_index) : 1}  # [x, y]
    end_reached = False
    line_counter = 1

    while not end_reached:
        print("progress: ", str(line_counter), " out of 141")
        next_beam_round = {}
        for beam_index in tachyon_beams.keys():
            try:
                resulting_beam_indices = process_beam(diagram, beam_index)
                for result in resulting_beam_indices:
                    hashable_result = "{0}, {1}".format(result[0], result[1])   # cursed I know
                    if hashable_result in next_beam_round.keys():
                        next_beam_round[hashable_result] = next_beam_round[hashable_result] + tachyon_beams[beam_index]
                    else:
                        next_beam_round[hashable_result] = tachyon_beams[beam_index]
            except:
                end_reached = True
        if not end_reached:
            tachyon_beams = next_beam_round
            line_counter += 1

    result = 0
    
    for final_beam_locash in tachyon_beams.keys():
        result += tachyon_beams[final_beam_locash]


    print(result)

main()