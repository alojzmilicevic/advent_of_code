from linereader import read_file

grid = [x for x in read_file('input.txt')]
H = len(grid)
W = len(grid[0])

# Find S
start_row = 0
start_col = grid[0].index('S')

queue = [(start_row, start_col)]
visited = set()
splits = 0

while queue:
    r, c = queue.pop(0)

    if (r, c) in visited:
        continue
    visited.add((r, c))

    cell = grid[r][c]

    if cell == '^':
        splits += 1

        if c - 1 >= 0:
            queue.append((r, c - 1))
        if c + 1 < W:
            queue.append((r, c + 1))
        
        # Do not continue downwards from a split
        continue
    
    if r + 1 < H:
        queue.append((r + 1, c))  # down

print(splits)