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


def check_validity(test_value, equations):
    is_valid = False
    for equation in equations:
        num_operations = len(equation) - 1
        num_permutations = 2 ** num_operations
        for i in range(0, num_permutations):
            mask = list(bin(i).split("b")[1])
            mask = [int(x) for x in mask]
            mask = [0] * (num_operations - len(mask)) + mask
            result = equation[0]
            for j in range(0, num_operations):
                if mask[j] == 0:
                    result += equation[j+1]
                if mask[j] == 1:
                    result *= equation[j+1]
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