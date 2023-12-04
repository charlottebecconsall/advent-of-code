/*
Whoever made the scratchcard rules was actually in elf land for real.
Also no wonder there's no snow, the number of scratchcards these elves are printing has clearly expedited climate change. 
*/

#include <stdio.h>

int SOLUTION_START_INDEX = 9;
int LOTTERY_START_INDEX = 41;
// int SOLUTION_START_INDEX = 7;
// int LOTTERY_START_INDEX = 24;

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
    int counter = 0;
    int card_number = 0;
    int card_counter_array[196] = {0};
    while (fgets(input_line, 128, input_file) != NULL) {
        card_counter_array[card_number] += 1;
        for (int i=SOLUTION_START_INDEX; i < LOTTERY_START_INDEX; i++) {
            if (is_digit(input_line[i]) && (input_line[i-1] == ' ')) {
                int winning_number = get_full_number(input_line + i);
                for (int j=LOTTERY_START_INDEX; input_line[j] != '\0'; j++) {
                    if (is_digit(input_line[j]) && (input_line[j-1] == ' ')) {
                        int lottery_number = get_full_number(input_line + j);
                        if (winning_number == lottery_number) { 
                            int num_cards = card_counter_array[card_number];
                            counter++; // Counts how many numbers are winning
                            card_counter_array[card_number + counter] += (num_cards);   // Adds one to the next card along
                        }
                    }
                }
            }
        }
        // Reset?
        card_number++;
        counter = 0;       
    }

    for (int i=0; i < 196; i++) {
        int card_count = card_counter_array[i];
        result += card_count;
    }

    printf("\nSUM: %d", result);

    return 0;
}