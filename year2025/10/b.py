from linereader import read_file
from common.parsing import extract_brackets, extract_parens, extract_braces
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

data = [x for x in read_file('input.txt')]

def read_line(line):
    indicator = [int(c == '#') for c in extract_brackets(line)]
    buttons = [[int(x) for x in btn.split(',')] for btn in extract_parens(line)]
    joltage = [int(x) for x in extract_braces(line).split(',')]
    
    return indicator, buttons, joltage

def solve_joltage(buttons, joltage):
    n_counters = len(joltage)
    n_buttons = len(buttons)
    
    A_eq = np.zeros((n_counters, n_buttons))
    for j, btn in enumerate(buttons):
        for counter_idx in btn:
            if counter_idx < n_counters:
                A_eq[counter_idx][j] = 1
    
    b_eq = np.array(joltage, dtype=float)
    
    c = np.ones(n_buttons)
    
    bounds = Bounds(lb=0, ub=np.inf)
    constraints = LinearConstraint(A_eq, b_eq, b_eq)
    
    integrality = np.ones(n_buttons) 
    
    result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)
    
    if result.success:
        return int(round(result.fun))
    else:
        return None

total = 0
for i in range(len(data)):
    _, buttons, joltage = read_line(data[i])
    presses = solve_joltage(buttons, joltage)
    total += presses

print(f"Total minimum button presses: {total}")
