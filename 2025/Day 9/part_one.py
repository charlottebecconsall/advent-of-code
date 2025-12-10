def parse_input(path):
    locations = []
    input = open(path, 'r')
    for line in input:
        line = line.split('\n')[0]
        line = line.split(',')
        locations.append(line)
    return locations


def get_area(location_1, location_2):
    x_diff = int(location_1[0]) - int(location_2[0]) + 1
    y_diff = int(location_1[1]) - int(location_2[1]) + 1

    area = x_diff * y_diff

    return area


def main():
    locations = parse_input("2025\Day 9\input.txt")
    areas = {}

    # fill grid
    for i in range(len(locations)):
        for j in range(len(locations)):
            if i != j:
                area = get_area(locations[i], locations[j])
                areas[area] = [locations[i], locations[j]]
    
    sorted_areas = []
    for area in areas.keys():
        sorted_areas.append(area)
    sorted_areas.sort(reverse=True)

    result = sorted_areas[0]

    print(result)

main()