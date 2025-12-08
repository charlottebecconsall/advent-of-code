import math

def parse_input(path):
    locations = []
    input = open(path, 'r')
    for line in input:
        line = line.split('\n')[0]
        line = line.split(',')
        locations.append(line)
    return locations


def get_distance(location_1, location_2):
    x_diff = int(location_1[0]) - int(location_2[0])
    y_diff = int(location_1[1]) - int(location_2[1])
    z_diff = int(location_1[2]) - int(location_2[2])

    distance = math.sqrt(x_diff**2 + y_diff**2 + z_diff**2)

    return distance


def main():
    locations = parse_input("2025\Day 8\input.txt")
    num_connections = len(locations)
    distances = {}
    circuits = {}
    num_circuits = 0
    result = 1

    # fill grid
    for i in range(len(locations)):
        for j in range(len(locations)):
            if i != j:
                distance = get_distance(locations[i], locations[j])
                distances[distance] = [locations[i], locations[j]]
    
    # connect x smallest distances together
    sorted_distances = []
    for distance in distances.keys():
        sorted_distances.append(distance)
    sorted_distances.sort()

    # and track circuits THIS IS THE DODGY PART
    for i in range(100000):
        connection_distance = sorted_distances[i]
        associated_locations = distances[connection_distance]

        if len(circuits.keys()) == 0:
            circuits[num_circuits] = associated_locations
            num_circuits += 1
        
        else:
            added_to_circuit = False
            added_to_circuit_id = ''
            for circuit_id in list(circuits.keys()):
                must_pop = False
                if added_to_circuit:
                    if associated_locations[0] in circuits[circuit_id] or associated_locations[1] in circuits[circuit_id]:
                        # merge the circuits
                        for item in circuits[circuit_id]:
                            if item not in circuits[added_to_circuit_id]:
                                circuits[added_to_circuit_id].append(item)
                        must_pop = True
                         
                if associated_locations[0] in circuits[circuit_id] and associated_locations[1] in circuits[circuit_id]:
                    added_to_circuit = True
                    added_to_circuit_id = circuit_id
                if associated_locations[0] in circuits[circuit_id] and associated_locations[1] not in circuits[circuit_id]:
                    circuits[circuit_id].append(associated_locations[1])
                    added_to_circuit = True
                    added_to_circuit_id = circuit_id
                if associated_locations[1] in circuits[circuit_id] and associated_locations[0] not in circuits[circuit_id]:
                    circuits[circuit_id].append(associated_locations[0])
                    added_to_circuit = True
                    added_to_circuit_id = circuit_id
                if must_pop:
                    circuits.pop(circuit_id)
            if not added_to_circuit:
                circuits[num_circuits] = associated_locations
                num_circuits += 1
                

        if len(circuits.keys()) == 1:
            if len(list(circuits.values())[0]) == num_connections:
                result *= int(associated_locations[0][0])
                result *= int(associated_locations[1][0])
                break
    
    circuit_sizes = []
    for circuit in circuits.keys():
        circuit_sizes.append(len(circuits[circuit]))
    circuit_sizes.sort(reverse=True)

    


    print(result)

main()