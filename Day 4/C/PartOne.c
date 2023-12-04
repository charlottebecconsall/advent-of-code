/*
Figuring out if the elves have won the lottery.
This time refusing to use anything other than stdio.h for no real reason.
Also there is likely a much better way to do this, I do not approve of the pyramid technique.
*/

#include <stdio.h>

int SOLUTION_START_INDEX = 9;
int LOTTERY_START_INDEX = 41;

/* Checks if a value is a digit */
int is_digit(char value) 
{
    if(value >= '0' && value <= '9') {
        return 1;
    } else {
        return 0;
    }
}

/* Get full number from the start index */ 
int get_full_number(char* input_line)
{
    int number = 0;
    for (int i=0; (is_digit(input_line[i])); i++) {
        number *= 10;
        number += input_line[i] - '0';
    }

    return number;
}

int main(void)
{
    char *filepath = "..\\input.txt";
    FILE *input_file = fopen(filepath, "r");
    char input_line[128];
    int result = 0;
    int counter = 1;
    int next_points = 0;
    while (fgets(input_line, 128, input_file) != NULL) {
        int next_points = 0;
        for (int i=SOLUTION_START_INDEX; i < LOTTERY_START_INDEX; i++) {
            if (is_digit(input_line[i]) && (input_line[i-1] == ' ')) {
                int winning_number = get_full_number(input_line + i);
                for (int j=LOTTERY_START_INDEX; input_line[j] != '\0'; j++) {
                    if (is_digit(input_line[j]) && (input_line[j-1] == ' ')) {
                        int lottery_number = get_full_number(input_line + j);
                        if (winning_number == lottery_number) {
                            if (next_points == 0) {next_points = 1;}
                            else {next_points *= 2;}
                        }
                    }
                }
            }
        }
        result += next_points;
        counter++;
        
    }

    printf("\nSUM: %d", result);

    return 0;
}