def parse_input():
    input = open("Day 7/input.txt", "r")
    equations = {}
    for line in input:
        line = line.strip("\n")
        test_value = int(line.split(":")[0])
        nums = line.split(":")[1]
        nums = nums.split()
        nums = [int(x) for x in nums]
        if test_value in equations.keys():
            equations[test_value].append(nums)
        else:
            equations[test_value] = []
            equations[test_value].append(nums)
    return equations

def translate_to_trinary(number, num_operations):
    array = [0] * num_operations
    i = num_operations - 1
    while number > 0:
        digit = number % 3
        array[i] = digit
        number = number - digit
        number = number / 3
        i -= 1
    return array

def check_validity(test_value, equations):
    is_valid = False
    for equation in equations:
        num_operations = len(equation) - 1
        num_permutations = 3 ** num_operations
        for i in range(0, num_permutations):
            trinary_representation = translate_to_trinary(i, num_operations)
            mask = trinary_representation
            result = equation[0]
            for j in range(0, num_operations):
                if mask[j] == 0:
                    result += equation[j+1]
                if mask[j] == 1:
                    result *= equation[j+1]
                if mask[j] == 2:
                    result = int(str(result) + str(equation[j+1]))
            if result == test_value:
                is_valid = True
    return is_valid


def main():
    equations = parse_input()
    sum_valids = 0
    for test_value in equations.keys():
        is_valid = check_validity(test_value, equations[test_value])
        if is_valid:
            sum_valids += test_value
            print("Test value", test_value, "has a valid equation")
    print(sum_valids)

main()