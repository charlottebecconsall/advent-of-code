def check_xmas(kernel):
    is_xmas = 0
    mas_check1 = kernel[0][0] + kernel[1][1] + kernel[2][2]
    mas_check2 = kernel[0][2] + kernel [1][1] + kernel[2][0]
    if (mas_check1 == "SAM" or mas_check1 == "MAS") and (mas_check2 == "SAM" or mas_check2 == "MAS"):
        is_xmas = 1
    return is_xmas


def main():
    with open("Day 4\input.txt", 'r') as file:
        input = file.read()
    input = input.split('\n')
    input = [list(x) for x in input]
    xmas_count = 0
    kernel_count = 0
    start_x = 0
    start_y = 0
    stop_x = 3
    stop_y = 3
    while stop_y <= len(input):
        kernel = []
        for y in range(start_y, stop_y):
            kernel.append(input[y][start_x:stop_x])
        if len(kernel[0]) != 3:
            start_y += 1
            stop_y += 1
            start_x = 0
            stop_x = 3
        if len(kernel[0]) == 3:
            xmas_count += check_xmas(kernel)
            kernel_count += 1
            start_x += 1
            stop_x += 1
    print(xmas_count)

main()