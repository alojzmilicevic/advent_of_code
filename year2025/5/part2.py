from linereader import read_file
data = [tuple(int(y) for y in x.split('-')) for x in read_file('input.txt')]

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged

d = merge_intervals(data)
print(d)

total = 0
for interval in d:
    total += interval[1] - interval[0] + 1

print(total)