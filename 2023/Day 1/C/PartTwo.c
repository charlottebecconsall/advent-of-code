#include <stdio.h>
#include <ctype.h>
#include <string.h>

char *numbers_spelling[] = {
    "one", "1", 
    "two", "2",
    "three", "3",
    "four", "4",
    "five", "5",
    "six", "6",
    "seven", "7",
    "eight", "8",
    "nine", "9"
};

char *translate_string(char *input_line)
{
    // insert the number found the index after the first letter of the word
    int translation_occurred = 1;
    while (translation_occurred == 1) {
        for (int i=0; numbers_spelling[i] != NULL; i+=2) {
            char *index = strstr(input_line, numbers_spelling[i]);
            translation_occurred = 0;
            if (index != NULL) {
                translation_occurred = 1;
                index++;
                *index = *numbers_spelling[i+1];
            }
            if (translation_occurred == 1) {
                i = -2;
            }
        }
    }

    return input_line;
}

int main()
{
    char *filepath = "..\\input.txt";
    FILE *input_file = fopen(filepath, "r");
    char input_line[128];
    int sum = 0;
    while (fgets(input_line, 128, input_file) != NULL) {
        char *translated_line = translate_string(input_line);
        int calibration_value = 0;
        int last_digit = 0;
        for (int i=0; translated_line[i] != '\0'; i++) {
            if (isdigit(translated_line[i])) {
                last_digit = translated_line[i] - '0';
                if (calibration_value == 0) {
                    calibration_value = (last_digit * 10);
                }
            }
        }
        sum = sum + calibration_value + last_digit;
    }

    printf("\n%d", sum);

    fclose(input_file);
    return 0;
}