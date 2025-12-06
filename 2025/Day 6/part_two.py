def parse_input(path):
    input = open(path, 'r')
    list_of_lines = []
    for line in input:
        line = line.removesuffix('\n')
        line = [list(num) for num in line]
        flattened_line = [num for sublist in line for num in sublist]
        list_of_lines.append(flattened_line)
    return list_of_lines

def cephalopodise_problem(problem):
    cephalopodised_problem = [problem[0].pop(-1)]
    for line in problem:
        true_number = ""
        for number in line:
            true_number += number
        true_number = int(true_number)
        cephalopodised_problem.append(true_number)
    return cephalopodised_problem

def transpose(input):
    problems = []
    for i in range(len(input[0])):
        problem = []
        for row in input:
            problem.append(row[i])
        problems.append(problem)
    return problems

def do_the_maths(problem):
    operation = problem.pop(0)
    if operation == "+":
        result = 0
        for num in problem:
            result += int(num)
    elif operation == "*":
        result = 1
        for num in problem:
            result *= int(num)
    else:
        result = 0
        print("operation not expected, received request for operation type ", operation)

    return result

def calculate(problems):
    full_problem = []
    result = 0
    for line in problems:
        break_test = [item == " " for item in line]
        if False in break_test:
            full_problem.append(line)
        else:
            problem = cephalopodise_problem(full_problem)
            result += do_the_maths(problem)
            full_problem = []
    problem = cephalopodise_problem(full_problem)
    result += do_the_maths(problem)
    return result
    

def main():
    list_of_lines = parse_input("2025\Day 6\input.txt")
    problems = transpose(list_of_lines)
    result = calculate(problems)
    print(result)

main()
