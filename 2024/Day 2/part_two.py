def analyse_report(report):
    safe = True
    if report[0] < report[1]:    # increasing
        for i in range(0, len(report)-1):
            diff = report[i+1] - report[i]
            if diff != 1 and diff != 2 and diff != 3:
                safe = False
                break
    else:    # decreasing/same
        for i in range(0, len(report)-1):
            diff = report[i] - report[i+1]
            if diff != 1 and diff != 2 and diff != 3:
                safe = False
                break
    return safe


def test_problem_dampener(report : list):
    safe = False
    for i in range(0, len(report)):
        test_report = report.copy()
        test_report.pop(i)
        safe = analyse_report(test_report)
        if safe:
            break
    return safe



def main():
    input = open("Day 2\input.txt", 'r')
    safe_reports = 0
    for line in input:
        line = list(map(int, line.split()))
        safe = analyse_report(line)
        if not safe:
            safe = test_problem_dampener(line)
        if safe:
            safe_reports += 1
    print(safe_reports)

main()
        