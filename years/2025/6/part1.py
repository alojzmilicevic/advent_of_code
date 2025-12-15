from linereader import read_file
import re
#data = read_file('test.input.txt')
data = read_file('input.txt')

matrix = []
ops = []



for line in data:
    raw_line = re.sub(r'\s+', ' ', line).strip().split(' ')

    if not raw_line[0].isnumeric():
        ops = raw_line
        break

    nums = [int(x) for x in raw_line]

    matrix.append(nums)


count = 0
for col in range(len(matrix[0])):
    col_total = 0
    operator = ops[col]
    for row in range(len(matrix)):
        if operator == '+':
            col_total += matrix[row][col]
        elif operator == '*':
            if col_total == 0:
                col_total = 1
            col_total *= matrix[row][col]

    count += col_total

print(count)