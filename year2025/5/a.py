from linereader import read_file

data = [x.split('-') for x in read_file('input.txt')]

def is_within_range(fruit_id, range):
    return range[0] <= fruit_id <= range[1]

count = 0
ranges = []

for line in data:
    if len(line) == 2:
        start = int(line[0])
        end = int(line[1])
        
        ranges.append((start, end))
    else:
        fruit_id = line[0]

        if fruit_id == '':
            continue
        else:
            for range in ranges:
                if is_within_range(int(fruit_id), range):
                    count += 1
                    break

total = 0
for range in ranges:
    total += range[1] - range[0]

print(total)

'''
3-5 10-14 12-18 16-20

'''
