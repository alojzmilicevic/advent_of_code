from linereader import read_file
from lib.point2d import Point2D


# -------------------------
# Point in polygon
# -------------------------

def point_on_segment(px, py, x1, y1, x2, y2):
    if not (min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2)):
        return False
    return abs((py - y1) * (x2 - x1) - (px - x1) * (y2 - y1)) < 1e-9


def point_in_polygon(px, py, poly):
    # boundary
    for i in range(len(poly)):
        x1, y1 = poly[i].x, poly[i].y
        x2, y2 = poly[(i + 1) % len(poly)].x, poly[(i + 1) % len(poly)].y
        if point_on_segment(px, py, x1, y1, x2, y2):
            return True

    inside = False
    j = len(poly) - 1
    for i in range(len(poly)):
        xi, yi = poly[i].x, poly[i].y
        xj, yj = poly[j].x, poly[j].y
        if ((yi > py) != (yj > py)) and \
                (px < (xj - xi) * (py - yi) / (yj - yi) + xi):
            inside = not inside
        j = i
    return inside


# -------------------------
# Largest rectangle in a binary matrix (DP)
# -------------------------

def histogram_largest_rectangle(heights):
    """Classic stack-based largest rectangle in histogram."""
    stack = []
    max_area = 0
    heights.append(0)

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            area = height * (i - left)
            max_area = max(max_area, area)
        stack.append(i)

    heights.pop()
    return max_area


# -------------------------
# Main computation
# -------------------------

points = [Point2D(*map(int, x.split(','))) for x in read_file("input.txt")]

# bounding box
xs = [p.x for p in points]
ys = [p.y for p in points]
xmin, xmax = min(xs), max(xs)
ymin, ymax = min(ys), max(ys)

W = xmax - xmin + 1
H = ymax - ymin + 1

# 1 = inside polygon, 0 = outside
grid = [[0] * W for _ in range(H)]

for y in range(H):
    py = ymin + y
    for x in range(W):
        px = xmin + x
        if point_in_polygon(px, py, points):
            grid[y][x] = 1


# Apply DP histogram method row by row
heights = [0] * W
best_area = 0

for row in grid:
    for j in range(W):
        heights[j] = heights[j] + 1 if row[j] == 1 else 0
    best_area = max(best_area, histogram_largest_rectangle(heights))

print(best_area)
