/*
Very confusing farming
*/

#include <stdio.h>
#include <ctype.h>

// #define NUM_SEEDS 4
#define MAPPINGS_SIZE 3

#define NUM_SEEDS 20

int get_numbers(char *input_line, long long *return_array, int return_array_len)
{
    long long number = 0;
    int counter = 0;
    int found_numbers = 0;
    for (int i=0; input_line[i] != '\n'; i++) {
        if (isdigit(input_line[i])) {
            found_numbers = 1;
            number *= 10;
            number += input_line[i] - '0';
            if ((input_line[i+1] == ' ') || (input_line[i+1] == '\n')) {
                return_array[counter] = number;
                number = 0;
                counter++;
            }
        } 

    }
    if (found_numbers == 0) {
        for (int i=0; i < return_array_len; i++) {
            return_array[i] = 0;
        }
    }
    return found_numbers;
}


int main(void) 
{
    char *filepath = "..\\input.txt";
    FILE *input_file = fopen(filepath, "r");
    char input_line[256];
    long long seeds[NUM_SEEDS];
    int seeds_padlock[NUM_SEEDS] = {0};
    long long mappings[MAPPINGS_SIZE];
    long long result = 0;

    fgets(input_line, 256, input_file);    // Initialises seeds
    get_numbers(input_line, seeds, NUM_SEEDS);
    while (fgets(input_line, 256, input_file) != NULL) {
        // Get a mapping
        int found_numbers = get_numbers(input_line, mappings, MAPPINGS_SIZE);
        for (int i=0; i < NUM_SEEDS; i++) {
            if ((mappings[1] <= seeds[i]) && (seeds[i] <= (mappings[1] + mappings[2])) && seeds_padlock[i] == 0) { 
                long long offset = seeds[i] - mappings[1];
                seeds[i] = mappings[0] + offset;
                seeds_padlock[i] = 1;
            }
        }
        if (found_numbers == 0) {for (int i=0; i<NUM_SEEDS; i++) {seeds_padlock[i] = 0;}}
    }
    result = seeds[0];
    for (int i=0; i < NUM_SEEDS; i++) {
        if (seeds[i] < result) {result = seeds[i];}
    }
    printf("%lld,", result);
    
}
