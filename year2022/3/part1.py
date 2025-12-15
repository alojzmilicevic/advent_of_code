from linereader import read_file
from string import ascii_letters

data = read_file('3.input.txt')





items = {}
alphabet = list(ascii_letters)

for line in data:
    first = line[:len(line) // 2]
    second = line[len(line) // 2:]

    for item in first:
        if item in items:
            items[item][0] += 1
        else:
            items.setdefault(item, [0, 0])
            items[item][0] = 1

    for item in second:
        if item in items:
            items[item][1] += 1
        else:
            items.setdefault(item, [0, 0])
            items[item][1] = 1

    items = {k: v for k, v in items.items() if v[0] != 0 and v[1] != 0}

total = 0
for key in items:
    print(key, alphabet.index(key) + 1)
    total += alphabet.index(key) + 1

print(total)
