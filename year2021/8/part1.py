from linereader import read_file

m = {
    2: [1],
    3: [7],
    4: []
}

numbersMap = {
    1: 2,
    4: 4,
    7: 4,
    2: 5,
    3: 5,
    5: 5,
    0: 6,
    6: 6,
    9: 6,
    8: 7,
}

d = [x.split('| ')[1].split(' ') for x in read_file('input.txt')]

total = 0
for line in d:
    for s in line:
        if len(s) == 2 or len(s) == 3 or len(s) == 4 or len(s) == 7:
            total += 1

print(total)
