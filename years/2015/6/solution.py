from common.grid import Grid
from common.solution import Solution
from lib.point2d import Point2D
import re

class Day(Solution):
    def part1(self):
        g = Grid(1000, 1000)
        for line in self.data:
            numbers = re.findall(r"\d+", line)
            a, b, c, d = map(int, numbers)
            p1 = Point2D(a, b)
            p2 = Point2D(c, d)

            if "toggle" in line:
                g.toggle_range(p1, p2)
            elif "turn on" in line:
                g.activate_range(p1, p2)
            else:
                g.deactivate_range(p1, p2)
        

        return g.sum()
    
    def part2(self):
        g = Grid(1000, 1000)
        for line in self.data:
            numbers = re.findall(r"\d+", line)
            a, b, c, d = map(int, numbers)
            p1 = Point2D(a, b)
            p2 = Point2D(c, d)

            if "toggle" in line:
                g.increment_range(p1, p2)
                g.increment_range(p1, p2)
            elif "turn on" in line:
                g.increment_range(p1, p2)
            else:
                g.decrement_range(p1, p2)   
        

        return g.sum()


Day().solve()
