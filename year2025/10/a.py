from linereader import read_file
from helpers import print_table
from common.parsing import extract_brackets, extract_parens, extract_braces

data = [x for x in read_file('test.input.txt')]

def create_matrix(indicator, buttons):
  n = len(indicator)
  m = len(buttons)

  matrix = [[0 for _ in range(m + 1)] for _ in range(n)]
  
  for y in range(n):
    for x in range(m):
      if y in buttons[x]:
        matrix[y][x] = 1
    # Add goal as last column, i cba swapping in two separate places 
    matrix[y][m] = indicator[y]

  return matrix


def combine_rows(pivot, target):
  row = []

  for i in range(len(pivot)):
    a = pivot[i]
    b = target[i]

    row.append(a ^ b)

  return row


def swap_rows(matrix, from_row, to_row):
  matrix[from_row], matrix[to_row] = matrix[to_row], matrix[from_row]

def read_line(line):
    indicator = [int(c == '#') for c in extract_brackets(line)]
    buttons = [[int(x) for x in btn.split(',')] for btn in extract_parens(line)]
    #joltage = [int(x) for x in extract_braces(line).split(',')]
    
    return indicator, buttons


for i in range(1):
    indicator, buttons = read_line(data[i])
    matrix = create_matrix(indicator, buttons)
    print_table(matrix)
    swap_rows(matrix, 0, 1)
    print_table(matrix)
