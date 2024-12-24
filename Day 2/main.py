# # Part 1
# input_file = 'input.txt'

# safeReports = 0

# with open(input_file, 'r') as file:
#     for report in file:
#         data = list(map(int, report.split()))
#         diffs = [data[i] - data[i + 1] for i in range(len(data) - 1)]
        
#         if all(
#             abs(diff) <= 3 and (all(d > 0 for d in diffs) or all(d < 0 for d in diffs))
#             for diff in diffs
#         ):
#             safeReports += 1

# print(safeReports)
# # >> safeReports = 279


# Part 2
input_file = 'input.txt'

safeReports = 0

def is_safe(data):
    """
    Check if the report is safe based on the rules.
    """
    diffs = [data[i + 1] - data[i] for i in range(len(data) - 1)]
    return all(
        1 <= abs(diff) <= 3 for diff in diffs
    ) and (all(d > 0 for d in diffs) or all(d < 0 for d in diffs))


with open(input_file, 'r') as file:
    for report in file:
        data = list(map(int, report.split()))

        # First, check if the report is safe
        if is_safe(data):
            safeReports += 1
        else:
            # Try removing each element and rechecking
            for i in range(len(data)):
                modified_data = data[:i] + data[i+1:]  # Remove the i-th element
                if is_safe(modified_data):
                    safeReports += 1
                    break  # If we find a safe configuration, stop checking further

print(safeReports)
# # >> safeReports = 343
