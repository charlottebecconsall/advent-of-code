import re

def check_horizontal(input):
    result = 0
    xmas_list = re.findall("XMAS", input)  
    result += len(xmas_list)
    samx_list = re.findall("SAMX", input)
    result += len(samx_list)
    return result

def check_vertical(input):
    split_input = input.split("\n")
    split_input = [list(x) for x in split_input]
    transposed = list(map(list, zip(*split_input)))
    transposed_inputtified = [''.join(x) for x in transposed]
    transposed_inputtified = '\n'.join(transposed_inputtified)
    result = check_horizontal(transposed_inputtified)
    return result

def check_diagonal1(input):
    split_input = input.split("\n")
    split_input = [list(x) for x in split_input]
    direction = "vertical"
    diagonalised_input = []
    if direction == "vertical":
        for y_index in range(0, len(split_input)):
            diagonalised_line = []
            for i in range(0, y_index+1):
                 diagonalised_line.append(split_input[y_index-i][i])
            diagonalised_input.append(diagonalised_line)
        direction = "horizontal"
    if direction == "horizontal":
        for x_index in range(1, len(split_input[0])-1):
            diagonalised_line = []
            x_offset = 0
            for y_index in range(len(split_input)-1, -1, -1):
                try:
                    diagonalised_line.append(split_input[y_index][x_index+x_offset])
                    x_offset += 1
                except:
                    continue    # this will skip the final corner but that should be fine right?
            diagonalised_input.append(diagonalised_line)
    diagonalised_inputtified = [''.join(x) for x in diagonalised_input]
    diagonalised_inputtified = '\n'.join(diagonalised_inputtified)
    result = check_horizontal(diagonalised_inputtified)
    return result


def check_diagonal2(input):
    split_input = input.split("\n")
    split_input = [list(x) for x in split_input]
    reversed_input = [list(reversed(x)) for x in split_input]
    inputtified = [''.join(x) for x in reversed_input]
    inputtified = '\n'.join(inputtified)
    result = check_diagonal1(inputtified)
    return result


def main():
    with open("Day 4\input.txt", 'r') as file:
        input = file.read()
    xmas_count = 0
    horizontal_count = check_horizontal(input)
    print("Horizontal count =", horizontal_count)
    xmas_count += horizontal_count
    vertical_count = check_vertical(input)
    print("Vertical count =", vertical_count)
    xmas_count += vertical_count
    diagonal1_count = check_diagonal1(input)
    print("Diagonal 1 count:", diagonal1_count)
    xmas_count += diagonal1_count
    diagonal2_count = check_diagonal2(input)
    print("Diagonal 2 count:", diagonal2_count)
    xmas_count += diagonal2_count


    print("Overall xmas count:", xmas_count)

main()
