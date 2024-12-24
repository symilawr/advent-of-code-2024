# Part 1
input_file = 'input.txt'

safeReports = 0

with open(input_file, 'r') as file:
    for report in file:
        data = list(map(int, report.split()))
        diffs = [data[i] - data[i + 1] for i in range(len(data) - 1)]
        
        if any(
            abs(diff) <= 3 and (all(d > 0 for d in diffs) or all(d < 0 for d in diffs))
            for diff in diffs
        ):
            safeReports += 1

print(safeReports)
# >> safeReports = 815
