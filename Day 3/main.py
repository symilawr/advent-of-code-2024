import re

input_file = 'input.txt'

def process_instructions(data):
    # Regex patterns
    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"  # Valid mul instructions
    control_pattern = r"do\(\)|don't\(\)"  # do() or don't() commands

    # Default state
    is_enabled = True
    total_sum = 0

    # Split the data into a sequence of instructions
    instructions = re.findall(f"{control_pattern}|{mul_pattern}", data)

    for instruction in instructions:
        if instruction == "don't()":
            # Disable future mul instructions
            is_enabled = False
        elif instruction == "do()":
            # Enable future mul instructions
            is_enabled = True
        elif re.fullmatch(mul_pattern, instruction) and is_enabled:
            # Process mul instructions only if enabled
            nums = instruction.replace('mul(', '').replace(')', '').split(',')
            x, y = map(int, nums)
            total_sum += x * y

    return total_sum

# Read the input file and calculate the result
with open(input_file, 'r') as file:
    content = file.read()

    # Calculate the sum of valid mul instructions
    result = process_instructions(content)
    print(result)

