from linereader import read_file
from lib.point2d import Point2D
import math

points = [Point2D(*map(int, x.split(','))) for x in read_file('input.txt')]

'''
tests = [
    (Point2D(2, 5), Point2D(9, 7), 24),
    (Point2D(7, 1), Point2D(11, 7), 35),
    (Point2D(7, 3), Point2D(2, 3), 6),
    (Point2D(2, 5), Point2D(11, 1), 50),
]

for a, b, expected in tests:
    dx = abs(a.x - b.x) + 1
    dy = abs(a.y - b.y) + 1
    assert dx * dy == expected

    print("Test passed: ", a, b, expected)
'''

max = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        a = points[i]
        b = points[j]
        dx = abs(a.x - b.x) + 1
        dy = abs(a.y - b.y) + 1
        if dx * dy > max:
            max = dx * dy
print(max)

