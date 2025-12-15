from linereader import read_file

data = read_file('input.txt')

points = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def loose(x):
    if x == 1:
        return 3
    elif x == 2:
        return 1

    return 2


total = 0
for line in data:
    a = points[line[0]]
    b = points[line[2]]

    if b == 1:  # loss
        total += loose(a)
    if b == 2:  # draw
        total += a
        total += 3
    if b == 3:  # win
        total += ((a % 3) + 3) % 3 + 1
        total += 6

print(total)
