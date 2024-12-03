import re

def main():
    input = open("Day 3\input.txt", 'r')
    mult_sum = 0
    for line in input:
        mults = re.findall("mul\([0-9]+,[0-9]+\)", line)
        for expression in mults:
            nums = expression[4:-1]
            nums = nums.split(",")
            result = int(nums[0]) * int(nums[1])
            mult_sum += result
    print(mult_sum)

main()