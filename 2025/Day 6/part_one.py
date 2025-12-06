def parse_input(path):
    input = open(path, 'r')
    list_of_lines = []
    for line in input:
        line = line.removesuffix('\n')
        line = line.split(' ')
        i = 1
        while i: 
            try:
                line.remove('')
            except ValueError:
                i = 0
        list_of_lines.append(line)
    return list_of_lines

def get_maths_problems(input):
    problems = []
    for i in range(len(input[0])):
        problem = []
        for row in input:
            problem.append(row[i])
        problems.append(problem)
    return problems

def do_the_maths(problem):
    operation = problem.pop(-1)
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



def main():
    list_of_lines = parse_input("2025\Day 6\input.txt")
    problems = get_maths_problems(list_of_lines)
    print(problems)
    result = 0
    for problem in problems:
        result += do_the_maths(problem)
    print(result)

main()
