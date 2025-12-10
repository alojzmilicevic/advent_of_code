from linereader import read_file

grid = [x for x in read_file('input.txt')]
H = len(grid)
W = len(grid[0])

# Find S
start_row = 0
start_col = grid[0].index('S')

ways = [[0]*W for _ in range(H)]
ways[start_row][start_col] = 1

ways = [[0]*W for _ in range(H)]
ways[start_row][start_col] = 1

for r in range(H):
    for c in range(W):
        if ways[r][c] == 0:
            continue

        cell = grid[r][c]

        if cell in ('.', 'S'):
            if r+1 < H:
                ways[r+1][c] += ways[r][c]

        elif cell == '^':
            if r+1 < H:
                if c-1 >= 0:
                    ways[r+1][c-1] += ways[r][c]
                if c+1 < W:
                    ways[r+1][c+1] += ways[r][c]

total_timelines = sum(ways[-1])
print(total_timelines)

