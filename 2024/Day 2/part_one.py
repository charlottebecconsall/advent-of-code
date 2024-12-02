def main():
    input = open("Day 2\input.txt", 'r')
    safe_reports = 0
    for line in input:
        line = list(map(int, line.split()))
        safe = True
        if line[0] < line[1]:    # increasing
            for i in range(0, len(line)-1):
                diff = line[i+1] - line[i]
                if diff != 1 and diff != 2 and diff != 3:
                    safe = False
                    break
        else:    # decreasing/same
            for i in range(0, len(line)-1):
                diff = line[i] - line[i+1]
                if diff != 1 and diff != 2 and diff != 3:
                    safe = False
                    break
        if safe:
            safe_reports += 1
    print(safe_reports)

main()
        