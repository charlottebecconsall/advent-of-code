/*
The oasis
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define PATTERN_LEN 21
// #define PATTERN_LEN 6

struct pattern
{
    int numbers_array[PATTERN_LEN];
    int differences_array[PATTERN_LEN];    // This should just store the last difference in the pattern
    int prediction;
};


void calculate_prediction(struct pattern *pattern) 
{
    int sum = 0;
    for (int i=0; i < PATTERN_LEN; i++) {
        sum += pattern->differences_array[i];
    }
    pattern->prediction = sum;
}


/* Creates an array of difference traces. Populates a pattern struct with the required information for the final solve*/
void get_differences(struct pattern *pattern)
{
    int differences[PATTERN_LEN];
    memcpy(differences, pattern->numbers_array, PATTERN_LEN*sizeof(int));
    for (int i=0; i < PATTERN_LEN; i++) {    // Goes through each layer of differences
        int difference = 0;
        for (int j=0; j < (PATTERN_LEN - (i+1)); j++) {    // Defines the next layer of differences
            difference = differences[j+1] - differences[j];;
            differences[j] = difference;
        }
    }
    memcpy(pattern->differences_array, differences, PATTERN_LEN*sizeof(int));

}


void create_numbers_array(char *input_line, int* numbers_array)
{
    for (int i=0; i < PATTERN_LEN; i++) {
        int number = strtol(input_line, &input_line, 10);
        numbers_array[i] = number;
    }

}


int main(void)
{
    char *filepath = "..\\input.txt";
    FILE *input_file = fopen(filepath, "r");
    char input_line[128];
    int result = 0;

    while (fgets(input_line, 128, input_file) != NULL) {
        int solved = 0;
        struct pattern pattern;
        create_numbers_array(input_line, pattern.numbers_array);
        get_differences(&pattern);
        calculate_prediction(&pattern);
        
        result += pattern.prediction;
    }
    printf("RESULT: %d", result);
}