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
        curIndex = (curIndex - steps) % 100
    elif direction == 'R':
        curIndex = (curIndex + steps) % 100

    if curIndex == 0:
        count += 1

print(count)