"""
Getting the first and last digit in a string
"""

def get_calibration_value(word:str):
    calibration_value = 0
    last_digit = ""
    for value in word:
        if value.isdigit():
            value = int(value)
            if last_digit == "":
                calibration_value += (value * 10)
            last_digit = value
    calibration_value += last_digit
    return calibration_value


def main(input_filepath):
    input_file = open(input_filepath)
    file_text = input_file.readlines()
    sum_of_calibration_values = 0
    for word in file_text:
        calibration_value = get_calibration_value(word)
        sum_of_calibration_values += calibration_value
    print(sum_of_calibration_values)


main("Day 1\input.txt")