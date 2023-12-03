/*
Find the sum of all numbers which are adjacent (including diagonally) to symbols, not including '.'
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

/* 
Checks if the number is a valid part number
Returns: part number if it is valid, 0 if part number not valid
*/
int get_part_number(int start_index, char *input_line, char *line_before, char *line_after)
 {
    // Get full number and index of end of number
    int number = 0;
    int end_index = start_index;
    for (end_index; (isdigit(input_line[end_index])); end_index++) {
        number *= 10;
        number += input_line[end_index] - '0';
    }
    end_index--;
    // printf("\nFull number found: %d", number);
    
    // Check all surrounding symbols
    int is_part = 0;
    for (int i=(start_index-1); i <= (end_index+1); i++) {
        if (i < 0) {
            continue;
        }
        if (is_symbol(line_before[i]) || is_symbol(input_line[i]) || is_symbol(line_after[i])) {
            is_part = 1;
        }
        // Check line before from start index - 1 to end index + 1
        // Check input line -1 to input line + 1
        // Check line after start index - 1 to end index + 1
    }

    if (is_part) {
        return number;
    }
    else {
        return 0;
    }
    // If an adjacent space contains a symbol, return the number found
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
        // printf("\nLine Before: %s", line_before);
        // printf("\nInput Line: %s", input_line);
        // printf("\nLine After: %s", line_after);
        // Do the actual calculating stuff
        int part_number = 0;
        for (int i=0; input_line[i] != '\0'; i++) {
            if (isdigit(input_line[i]) && (!isdigit(input_line[i-1]))) {
                part_number = get_part_number(i, input_line, line_before, line_after);
                sum += part_number;
                if(part_number > 0) {
                    printf("%d,", part_number);
                }

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
