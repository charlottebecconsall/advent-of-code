/*
Find the sum of all products of numbers which are adjacent (including diagonally) to a *, where there are exactly 2 numbers.
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Checks if character is a valid symbol
int is_symbol(char character)
{
    int symbol = 0;
    if ((character < '0') || ((character > '9') && (character < 'A')) || ((character > 'Z') && (character < 'a')) || (character > 'z')) 
    {
        if ((character != '.') && (character != '\n')) {
            symbol = 1;
        }
    }
    return symbol;
}

// Gets full number
int get_full_number(int start_index, char *input_line)
{
    // Get full number and index of end of number
    int number = 0;
    for (start_index; (isdigit(input_line[start_index])); start_index++) {
        number *= 10;
        number += input_line[start_index] - '0';
    }
    
    return number;
}

/* 
Checks if there's a valid gear ratio
Returns: gear ratio if it is valid, 0 if part number not valid
*/
int get_gear_ratio(int asterisk_index, char *input_line, char *line_before, char *line_after)
 {
    // Check all surrounding areas for a number
    // If a number is found, record the index of that number and what line the number is on (working on this)
    // Find the full number
    // If more than two full numbers have been found, set the return value to zero
    // Get product of those two numbers and return it
    int gear_ratio = 1;

    // Check all surrounding spaces
    int first_number_index = -1;
    char *first_number_line[156];
    int second_number_index = -1;
    char *second_number_line[156];
    for (int i=(asterisk_index-1); i <= (asterisk_index+1); i++) {
        if (i < 0) {
            continue;
        }
        if (isdigit(line_before[i]) || isdigit(input_line[i]) || isdigit(line_after[i])) {
            if (first_number_index == -1) {
                if (second_number_index == -1) {gear_ratio = 0;}
                else {second_number_index = i;} // TODO assign second number line to the right line
            }
        }
    }
    
    
    return gear_ratio;
 }


int main(void)
{
    char *filepath = "..\\input.txt";
    FILE *input_file_ptr_1 = fopen(filepath, "r");
    FILE *input_file_ptr_2 = fopen(filepath, "r");
    char input_line[156];
    char line_before[156];
    char line_after[156];
    int sum = 0;

    fgets(input_line, 156, input_file_ptr_2);
    strcpy(line_before, input_line);
    while (fgets(input_line, 156, input_file_ptr_1) != NULL) {
        fgets(line_after, 156, input_file_ptr_2);    //ptr_2 is one ahead of ptr_1
        int gear_ratio = 0;
        for (int i=0; input_line[i] != '\0'; i++) {
            // if it finds an asterisk, get 'gear ratio'
            if (input_line[i] == '*') {
                gear_ratio = get_gear_ratio(i, input_line, line_before, line_after);
                sum += gear_ratio;
            }
            
        }
        // Change everything around
        strcpy(line_before, input_line);
        printf("\n");
        
    }
    // there's a potential bug where it will struggle with the very last line.
    fclose(input_file_ptr_1);
    fclose(input_file_ptr_2);

    printf("\nSUM: %d", sum);

    return 0;
}
