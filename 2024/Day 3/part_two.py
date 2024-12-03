import re

def calculate_mults(line):
    mults = re.findall("mul\([0-9]+,[0-9]+\)", line)
    result_sum = 0
    for expression in mults:
        nums = expression[4:-1]
        nums = nums.split(",")
        result = int(nums[0]) * int(nums[1])
        result_sum += result
    return result_sum

def main():
    with open("Day 3\input.txt", 'r') as file:
        input = file.read().replace('\n', "ye")
    mult_sum = 0
    # split at the don'ts
    split_at_donts = input.split("don't()")
    unaffected_mults = calculate_mults(split_at_donts[0])
    mult_sum += unaffected_mults
    # split at dos
    for i in range(1, len(split_at_donts)):
        do_splits = split_at_donts[i].split("do()")
        for x in range(1, len(do_splits)):
            result = calculate_mults(do_splits[x])
            mult_sum += result
        
    print(mult_sum)

main()
