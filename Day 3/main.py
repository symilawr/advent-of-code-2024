import re

input_file = 'input.txt'

with open(input_file, 'r') as file:
    content = file.read()
    
    # Regex pattern
    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    # Find all matches
    matches = re.findall(pattern, content)
    sum_match = 0
    for match in matches:
        nums = match.replace('mul(','').replace(')','').split(',')
        x, y = map(int, nums)
        product = int(x) * int(y)
        sum_match = sum_match + product
    print(sum_match)

