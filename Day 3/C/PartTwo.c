/*
Find the sum of all products of numbers which are adjacent (including diagonally) to a *, where there are exactly 2 numbers.
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>


struct gear_number 
{
    int number;
    int start_index;
    int end_index;
};


/*
Checks if character is a valid symbol
*/
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
Gets full number, given an index which lies somewhere in that number
Returns: full number found, start index of number in line provided, end index of number in line provided
*/
struct gear_number get_full_number(int index, char *input_line)
{
    int number = 0;
    int start_index = 0;
    if (index != 0) {
        // Find the start index of the number
        for (int i=0; isdigit(input_line[index-i]); i++) {
            if ((index-i) == 0) {start_index = 0;}
            else if (!isdigit(input_line[index-(i+1)])) {start_index = index - i;}
        }
    } else {start_index = index;}

    // Get full number from the start index
    int end_index = start_index;
    for (end_index; (isdigit(input_line[end_index])); end_index++) {
        number *= 10;
        number += input_line[end_index] - '0';
    }
    
    struct gear_number gear_information = {number, start_index, end_index};
    return gear_information;
}

/* 
Checks if there's a valid gear ratio
Returns: gear ratio if it is valid, 0 if part number not valid
*/
int get_gear_ratio(int asterisk_index, char *input_line, char *line_before, char *line_after)
 {
    int gear_ratio = 1;
    int counter = 0;
    char *lines[3] = {line_before, input_line, line_after};
    struct gear_number gear_information;
    for (int line_num=0; line_num < 3; line_num++) {
        char *line = lines[line_num];
        for (int i=(asterisk_index-1); i <= (asterisk_index+1); i++) {
            if (i < 0) {continue;}
            if (isdigit(line[i])) {
                gear_information = get_full_number(i, line);
                gear_ratio *= gear_information.number;
                counter++;
                i = gear_information.end_index;
            }
        }
    }

    if (counter != 2) {
        gear_ratio = 0;
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
        strcpy(line_before, input_line);
        printf("\n");
        
    }
    fclose(input_file_ptr_1);
    fclose(input_file_ptr_2);

    printf("\nSUM: %d", sum);

    return 0;
}
