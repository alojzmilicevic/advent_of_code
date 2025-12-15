def path(wire):
    total = {}
    end = [0, 0]
    num_steps = 1
    wired = set()

    for way in wire:
        direction = way[0]
        dist = int(way[1:])

        if direction == 'R':
            for moved in range(1, dist + 1):
                wired.add((moved + end[0], end[1]))
                total[(moved + end[0], end[1])] = num_steps
                num_steps += 1
            end[0] = dist + end[0]

        elif direction == 'U':
            for moved in range(1, dist + 1):
                wired.add((end[0], moved + end[1]))
                total[(end[0], moved + end[1])] = num_steps
                num_steps += 1
            end[1] = dist + end[1]

        elif direction == 'L':
            for moved in range(1, dist + 1):
                wired.add((end[0] - moved, end[1]))
                total[(end[0] - moved, end[1])] = num_steps
                num_steps += 1
            end[0] = end[0] - dist

        elif direction == 'D':
            for moved in range(1, dist + 1):
                wired.add((end[0], end[1] - moved))
                total[(end[0], end[1] - moved)] = num_steps
                num_steps += 1
            end[1] = end[1] - dist

    return wired, total


with open('input.txt') as f:
    wire_paths = [path.split(',') for path in f.read().split()]

p1, num_steps_1 = path(wire_paths[0])
p2, num_steps_2 = path(wire_paths[1])
intersections = p1 & p2

nearest = None
for X in intersections:
    distance = abs(X[0]) + abs(X[1])
    if not nearest or distance < nearest:
        nearest = distance

# 1
print(nearest)

min_steps = None
for X in intersections:
    combined_steps = num_steps_1[X] + num_steps_2[X]
    if not min_steps or combined_steps < min_steps:
        min_steps = combined_steps

# 2
print(min_steps)
