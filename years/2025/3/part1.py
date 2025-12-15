import sys
sys.path.insert(0, '../../')
from linereader import read_file

from itertools import combinations

data = [x for x in read_file('input.txt')]

NUM_BATTERIES = 12

total = 0

for row in data:
    max_joltage = 0
    
    # Check all combinations of NUM_BATTERIES indices
    for indices in combinations(range(len(row)), NUM_BATTERIES):
        # Form the number from selected batteries
        joltage_str = ''.join(row[i] for i in indices)
        joltage = int(joltage_str)
        if joltage > max_joltage:
            max_joltage = joltage
    
    print(f"{row}: {max_joltage}")
    total += max_joltage

print(f"\nTotal output joltage: {total}")
        

    
