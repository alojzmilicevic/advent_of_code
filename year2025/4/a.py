from linereader import read_file

data = [list(x) for x in read_file('input.txt')]

def scanNeighbors(x, y, grid):
    neighbors = []
    for i in range(x - 1, x + 2):
        if i < 0 or i >= len(grid):
            continue
        
        for j in range(y - 1, y + 2):
            if j < 0 or j >= len(grid[0]):
                continue
            if j == y and i == x:
                continue
        
            if grid[i][j] == '@':
                neighbors.append((i, j))

    return len(neighbors) < 4



def run(data):
    count = 0
    marked = []

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '@':
                if scanNeighbors(i, j, data):
                    count += 1
                    marked.append((i, j))
    
    return count, marked

def clear_marked(data, marked):
    for i in marked:
        data[i[0]][i[1]] = '.'

total = 0
while True:
    count, marked = run(data)
    clear_marked(data, marked)
    print(count)
    total += count
    if count == 0:
        break

print(total)