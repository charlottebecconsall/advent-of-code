"""Getting the first and last digit in a string, even if the digits are spelt as numbers"""

number_spellings = {
    "one": 1, 
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
    }

def translate_input_word(word:str):
    index_dict = {}
    new_word = list(word)
    for number in number_spellings.keys():
        if number in word:
            first_index = word.index(number)
            new_word[first_index] = str(number_spellings[number])
            last_index = word.rindex(number)
            new_word[last_index] = str(number_spellings[number])
    return new_word


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
        word = translate_input_word(word)
        calibration_value = get_calibration_value(word)
        sum_of_calibration_values += calibration_value
    print(sum_of_calibration_values)

main("Day 1\input.txt")