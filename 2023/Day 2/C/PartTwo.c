/*
Find the minimum set of cubes for each game.
Answer is sum of the 'powers' of the cubes (each colour multiplied)
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>


int find_minimum_set(char *game_line)
{
    game_line = strstr(game_line, ":");
    // These numbers will hold the maximum for each found
    int red = 0;
    int green = 0;
    int blue = 0;

    int digit = 0;
    for (int i=0; game_line[i] != '\0'; i++) {
        // if a digit is found, keep it safe
        if (isdigit(game_line[i])) {
            if (digit != 0) {
                digit *= 10;
            } 
            digit += (game_line[i] - '0');
            // once a full number has been found, find out where it should go
            if (game_line[i+1] == ' ') {
                char colour = game_line[i+2];
                if ((colour == 'r') && (digit > red)) {
                    red = digit;
                } else if ((colour == 'g') && (digit > green)) {
                    green = digit;
                } else if ((colour == 'b') && (digit > blue)) {
                    blue = digit;
                }
                digit = 0;
            }
        }        
    }

    return (red * green * blue);
}


int main(void) 
{
    char *filepath = "..\\input.txt";
    FILE *input_file = fopen(filepath, "r");
    int sum = 0;
    char game_line[256];
    while (fgets(game_line, 256, input_file) != NULL) {
        int cubes_power = find_minimum_set(game_line);
        sum += cubes_power;
    }
    printf("\n%d", sum);
    return 0;
}