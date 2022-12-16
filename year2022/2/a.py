from linereader import read_file

data = read_file('2.input.txt')

points = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}

total = 0

for line in data:
    a = points[line[0]]
    b = points[line[2]]

    total += b

    if a == b:
        total += 3
    else:
        comp = b - 1

        if comp == 0:
            comp = 3

        if comp == a:
            total += 6

print(total)
