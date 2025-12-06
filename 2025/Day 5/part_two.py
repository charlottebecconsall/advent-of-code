def parse_input(path):
    fresh_ranges = []
    input = open(path, 'r')
    for line in input:
        if "-" in line:
            fresh_ranges.append(line.split('\n')[0])
    return fresh_ranges


def main():
    fresh_ranges = parse_input("2025\Day 5\input.txt")

    non_overlapped_ranges = []

    for fresh_range in fresh_ranges:
        start = int(fresh_range.split('-')[0])
        stop = int(fresh_range.split('-')[1])
        i = 0
        for range in non_overlapped_ranges:
            if start >= range[0] and start <= range[1]: 
                if stop > range[1]:   
                    start = range[1] + 1    
            if stop >= range[0] and stop <= range[1]:   
                stop = range[0] - 1
            if start >= range[0] and stop <=range[1]:
                stop = 0
                start = 0
            if range[0] >= start and range[1] <= stop:
                non_overlapped_ranges.pop(i)
            i += 1
        if (stop + start) > 0:
            non_overlapped_ranges.append([start, stop])
    
    fresh_ingredient_ids = 0
    for range in non_overlapped_ranges:
        fresh_ingredient_ids += range[1] - range[0] + 1
    
    print(fresh_ingredient_ids)
        
    

main()