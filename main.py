# Part 1
input_file = 'input.txt'

safeReports = 0

with open(input_file, 'r') as file:
    for report in file:
        data = list(map(int, report.split()))
        diffs = [data[i + 1] - data[i] for i in range(len(data) - 1)]
        
        # Check if all differences are between 1 and 3, and all are either positive or negative
        if all(1 <= abs(diff) <= 3 for diff in diffs) and (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)):
            safeReports += 1

print(safeReports)
