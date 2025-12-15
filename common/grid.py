from typing import List, Any
from io import StringIO
import sys
from .grid_printer import print_colored_grid
from lib.point2d import Point2D

class Grid:
    def __init__(self, n: int, m: int) -> None:
        self.n: int = n
        self.m: int = m
        self.count = 0
        self.grid: List[List[Any]] = [[0 for _ in range(m)] for _ in range(n)]
    
    def __str__(self) -> str:
        old_stdout = sys.stdout
        sys.stdout = buffer = StringIO()
        try:
            print_colored_grid(self.grid)
            output = buffer.getvalue()
        finally:
            sys.stdout = old_stdout
        return output.rstrip()
    
    def toggle_point(self, p: Point2D):
        if self.grid[p.y][p.x] == 0:
            self.count += 1
        else:
            self.count -= 1
        self.grid[p.y][p.x] ^= 1
    
    def toggle_range(self, p1: Point2D, p2: Point2D):
        x_min, y_min, x_max, y_max = (
            min(p1.x, p2.x),
            min(p1.y, p2.y),
            max(p1.x, p2.x) + 1,
            max(p1.y, p2.y) + 1,
        )
        for y in range(y_min, y_max):
            for x in range(x_min, x_max):
                self.toggle_point(Point2D(x, y))
    
    def activate_point(self, p: Point2D):
        if self.grid[p.y][p.x] == 0:
            self.count += 1
        self.grid[p.y][p.x] = 1
    
    def activate_range(self, p1: Point2D, p2: Point2D):
        x_min, y_min, x_max, y_max = (
            min(p1.x, p2.x),
            min(p1.y, p2.y),
            max(p1.x, p2.x) + 1,
            max(p1.y, p2.y) + 1,
        )
        for y in range(y_min, y_max):
            for x in range(x_min, x_max):
                self.activate_point(Point2D(x, y))
    
    def deactivate_point(self, p: Point2D):
        if self.grid[p.y][p.x] == 1:
            self.count -= 1
        self.grid[p.y][p.x] = 0
    
    def deactivate_range(self, p1: Point2D, p2: Point2D):
        x_min, y_min, x_max, y_max = (
            min(p1.x, p2.x),
            min(p1.y, p2.y),
            max(p1.x, p2.x) + 1,
            max(p1.y, p2.y) + 1,
        )
        for y in range(y_min, y_max):
            for x in range(x_min, x_max):
                self.deactivate_point(Point2D(x, y))
    
    def increment_point(self, p: Point2D):
        self.grid[p.y][p.x] += 1
        self.count += 1
    
    def increment_range(self, p1: Point2D, p2: Point2D):
        x_min, y_min, x_max, y_max = (
            min(p1.x, p2.x),
            min(p1.y, p2.y),
            max(p1.x, p2.x) + 1,
            max(p1.y, p2.y) + 1,
        )
        for y in range(y_min, y_max):
            for x in range(x_min, x_max):
                self.increment_point(Point2D(x, y))
    
    def decrement_point(self, p: Point2D):
        if self.grid[p.y][p.x] > 0:
            self.grid[p.y][p.x] -= 1
            self.count -= 1
    
    def decrement_range(self, p1: Point2D, p2: Point2D):
        x_min, y_min, x_max, y_max = (
            min(p1.x, p2.x),
            min(p1.y, p2.y),
            max(p1.x, p2.x) + 1,
            max(p1.y, p2.y) + 1,
        )
        for y in range(y_min, y_max):
            for x in range(x_min, x_max):
                self.decrement_point(Point2D(x, y))

    def sum(self):
        return self.count