from linereader import read_file
from lib.point2d import Point2D
from common.grid_printer import print_colored_grid, Colors

points = [Point2D(*map(int, x.split(','))) for x in read_file('test.input.txt')]

x_min = min(points, key=lambda x: x.x).x
x_max = max(points, key=lambda x: x.x).x

y_min = min(points, key=lambda x: x.y).y
y_max = max(points, key=lambda x: x.y).y

# init grid
grid = [[0 for _ in range(x_max + 2)] for _ in range(y_max + 2)]

def make_grid():
# mark the points in the grid
    for pIdx in range(len(points)):
        point = points[pIdx]
        grid[point.y][point.x] = 1

        next_point = None
        if pIdx < len(points) - 1:
            next_point = points[pIdx + 1]
        elif pIdx == len(points) - 1:
            next_point = points[0]


        if next_point.y == point.y:
            #traverse x
            min_x = min(point.x, next_point.x)
            max_x = max(point.x, next_point.x)
            for x in range(min_x + 1, max_x):
                grid[point.y][x] = 2
        elif next_point.x == point.x:
            #traverse y
            min_y = min(point.y, next_point.y)
            max_y = max(point.y, next_point.y)
            for y in range(min_y + 1, max_y):
                grid[y][point.x] = 2
                
make_grid()

def point_in_polygon(px, py, polygon):
    inside = False
    p1 = polygon[0]
    
    for i in range(1, len(polygon) + 1):
        p2 = polygon[i % len(polygon)]
        
        # Skip horizontal edges (don't cross horizontal ray)
        if p1.y == p2.y:
            p1 = p2
            continue
            
        # Check if edge crosses the ray
        if py > min(p1.y, p2.y) and py <= max(p1.y, p2.y):
            if px <= max(p1.x, p2.x):
                x_intersection = (py - p1.y) * (p2.x - p1.x) / (p2.y - p1.y) + p1.x
                if p1.x == p2.x or px <= x_intersection:
                    inside = not inside
        
        p1 = p2
    
    return inside

for y in range(y_max + 2):
    for x in range(x_max + 2):
        if grid[y][x] == 1 or grid[y][x] == 2:
            continue
        
        if point_in_polygon(x, y, points):
            grid[y][x] = 2

print_colored_grid(grid, {
    0: Colors.BLACK,
    1: Colors.RED,
    2: Colors.GREEN
})