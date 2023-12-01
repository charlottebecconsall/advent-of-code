#include <stdio.h>
#include <ctype.h>

int main()
{
    char *filepath = "..\\input.txt";
    FILE *input_file = fopen(filepath, "r");
    char input_line[128];
    int sum = 0;
    while (fgets(input_line, 128, input_file) != NULL) {
        int calibration_value = 0;
        int last_digit = 0;
        for (int i=0; input_line[i] != '\0'; i++) {
            if (isdigit(input_line[i])) {
                last_digit = input_line[i] - '0';
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