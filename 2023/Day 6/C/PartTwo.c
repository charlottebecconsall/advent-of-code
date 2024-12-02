/*
We racing boats now
*/

#include <stdio.h>
#include <math.h>
#include <ctype.h>

// #define NUM_RACES 3
#define NUM_RACES 1

struct boat_race 
{
    long long time;
    long long distance;
};


void get_boat_race_info(struct boat_race *races, char *time_info, char *distance_info) 
{
    long long time = 0;
    long long distance = 0;
    int counter = 0;
    for (int i=0; distance_info[i] != '\n'; i++) {
        if (isdigit(time_info[i])) {
            time *= 10;
            time += time_info[i] - '0';
            if (distance_info[i+1] == '\n') {
                races[counter].time = time;
                time = 0;
            }
        }
        if (isdigit(distance_info[i])) {
            distance *= 10;
            distance += distance_info[i] - '0';
            if (distance_info[i+1] == '\n') {
                races[counter].distance = distance;
                distance = 0;
                counter++;
            }
        }
    }
}


int main(void)
{
    char *filepath = "..\\input.txt";
    FILE *input_file = fopen(filepath, "r");
    char time_info[128];
    char distance_info[128];
    int result = 1;
    struct boat_race races[NUM_RACES];

    fgets(time_info, 128, input_file);
    fgets(distance_info, 128, input_file);

    get_boat_race_info(races, time_info, distance_info);

    for (int i=0; i < NUM_RACES; i++) {
        double d = (races[i].time * races[i].time) - (4 * 1 * (races[i].distance + 1));
        long long low_num = ceil((-races[i].time + sqrt(d)) / -2);
        long long high_num = floor((-races[i].time - sqrt(d)) / -2);
        printf("Low num: %lld\n", low_num);
        printf("High num: %lld\n", high_num);
        result *= high_num - low_num + 1;
    }

    printf("%d", result);
    
    return 0;
}