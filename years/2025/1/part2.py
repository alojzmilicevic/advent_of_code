import sys
sys.path.insert(0, '../../')
from linereader import read_file

data = [x for x in read_file('input.txt')]

curIndex = 50
count = 0

for item in data:
    direction = item[0]
    steps = int(item[1:])

    if direction == 'L':
        if curIndex == 0:
            count += steps // 100
        elif steps >= curIndex:
            count += 1 + (steps - curIndex) // 100
        curIndex = (curIndex - steps) % 100
    elif direction == 'R':
        if curIndex == 0:
            count += steps // 100
        elif steps >= 100 - curIndex:
            count += 1 + (steps - (100 - curIndex)) // 100
        curIndex = (curIndex + steps) % 100

print(count)