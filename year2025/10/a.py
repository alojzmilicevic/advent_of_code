from linereader import read_file
from common.parsing import extract_brackets, extract_parens, extract_braces
from itertools import combinations

data = [x for x in read_file('input.txt')]

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
    joltage = [int(x) for x in extract_braces(line).split(',')]
    
    return indicator, buttons, joltage

def gf2_rref(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0]) - 1
    pivot_info = []
    row = 0

    for col in range(n_cols):
        pivot_row = None
        for r in range(row, n_rows):
            if matrix[r][col] == 1:
                pivot_row = r
                break
        if pivot_row is None:
            continue

        if pivot_row != row:
            swap_rows(matrix, pivot_row, row)

        pivot_info.append((row, col))

        for r in range(row + 1, n_rows):
            if matrix[r][col] == 1:
                matrix[r] = combine_rows(matrix[row], matrix[r])

        row += 1

    for pivot_row, pivot_col in reversed(pivot_info):
        for r in range(pivot_row):
            if matrix[r][pivot_col] == 1:
                matrix[r] = combine_rows(matrix[pivot_row], matrix[r])

    return pivot_info

total = 0
for i in range(len(data)):
    indicator, buttons, joltage = read_line(data[i])
    matrix = create_matrix(indicator, buttons)
    pivot_info = gf2_rref(matrix)
    
    n_cols = len(matrix[0]) - 1
    pivot_cols = set(col for _, col in pivot_info)
    free_cols = [col for col in range(n_cols) if col not in pivot_cols]
    
    min_presses = None
    
    for num_free_pressed in range(len(free_cols) + 1):
        for pressed_free_cols in combinations(free_cols, num_free_pressed):
            solution = [0] * n_cols
            
            for col in pressed_free_cols:
                solution[col] = 1
            
            for pivot_row, pivot_col in reversed(pivot_info):
                val = matrix[pivot_row][-1]
                for col in range(n_cols):
                    if col != pivot_col:
                        val ^= (matrix[pivot_row][col] * solution[col])
                solution[pivot_col] = val
            
            presses = sum(solution)
            if min_presses is None or presses < min_presses:
                min_presses = presses
    
    total += min_presses
    
print(f"Total minimum button presses: {total}")


