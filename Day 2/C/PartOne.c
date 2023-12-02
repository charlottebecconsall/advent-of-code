/*
Which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
Answer is sum of possible game IDs.

As it turns out, I did overcomplicate this oops
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>


int MAX_RED = 12;
int MAX_GREEN = 13;
int MAX_BLUE = 14;


int get_game_id(char *game_line)
{
    int game_id = 0;
    char *id_ptr = strstr(game_line, ":");
    game_id = strtol((game_line+5), &id_ptr, 10);

    return game_id;
}


int check_possibility(char *game_line)
{
    int is_possible = 1;
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
                if (colour == 'r') {
                    red += digit;
                } else if (colour == 'g') {
                    green += digit;
                } else if (colour == 'b') {
                    blue += digit;
                }
                digit = 0;
            }
        }
        // if a semicolon or a colon is reached, evaluate if the game is possible
        if ((game_line[i] == ':') | (game_line[i] == ';') | (game_line[i] == '\n')) {
            if ((red > MAX_RED) | (green > MAX_GREEN) | (blue > MAX_BLUE)) {
                is_possible = 0;
            }
            // Reset for the next set
            red = 0;
            green = 0;
            blue = 0;
            digit = 0;
        }
        
    }

    return is_possible;
}


int main(void) 
{
    char *filepath = "..\\input.txt";
    FILE *input_file = fopen(filepath, "r");
    int sum = 0;
    char game_line[256];
    while (fgets(game_line, 256, input_file) != NULL) {
        int game_id = get_game_id(game_line);
        int is_possible = check_possibility(game_line);
        if (is_possible) {
            sum += game_id;
        }
    }
    printf("\n%d", sum);
    return 0;
}