import sys
sys.path.insert(0, '../../')
from linereader import read_line

data = [x for x in read_line('input.txt', ",")]

def is_even(n):
    return len(n) % 2 == 0
    
def get_parts(s):
    mid = len(s) // 2
    return s[:mid], s[mid:]

count = 0
for r in data:
    parts = r.split("-")
    first = int(parts[0])
    second = int(parts[1])

    for i in range(first, second + 1):
        s = str(i)

        if is_even(s):
            left, right = get_parts(s)
            if left == right:
                count += i
        

print(count)