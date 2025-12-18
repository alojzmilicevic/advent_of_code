from common.solution import Solution
import sys


class Day(Solution):
    def is_local_min(self, row, col, arr):
        height = len(arr)
        width = len(arr[0])
        
        north = sys.maxsize
        south = sys.maxsize
        east = sys.maxsize
        west = sys.maxsize
        
        cur = arr[row][col]
        
        if row > 0:
            north = arr[row - 1][col]
        
        if row < (height - 1):
            south = arr[row + 1][col]
        
        if col > 0:
            west = arr[row][col - 1]
        
        if col < (width - 1):
            east = arr[row][col + 1]
        
        return cur < north and cur < south and cur < east and cur < west
    
    def part1(self):
        d = [[int(y) for y in list(x)] for x in self.data]
        
        risk_level = 0
        for i in range(len(d)):
            for j in range(len(d[i])):
                if self.is_local_min(i, j, d):
                    risk_level += d[i][j] + 1
        
        return risk_level
    
    def get_lowest_points(self, data):
        potential = []
        
        for i, row in enumerate(data):
            positions = sorted(range(len(row)), key=lambda x: row[x])
            reserved = []
            for pos in positions:
                if pos + 1 in reserved or pos - 1 in reserved:
                    continue
                
                cond1 = row[pos - 1] > row[pos] if pos - 1 >= 0 else True
                cond2 = row[pos + 1] > row[pos] if pos + 1 < len(row) else True
                if cond1 and cond2:
                    reserved.append(pos)
                    potential.append((i, pos))
        
        coords = []
        for x, y in potential:
            value = data[x][y]
            cond1 = data[x - 1][y] > value if x - 1 >= 0 else True
            cond2 = data[x + 1][y] > value if x + 1 < len(data) else True
            if cond1 and cond2:
                coords.append((x, y))
        
        return coords
    
    def flood_fill_util(self, data, x, y, points, visited, width, height):
        if x < 0 or x >= width:
            return
        
        if y < 0 or y >= height:
            return
        
        if data[y][x] == 9 or ((y * width) + x) in visited:
            return
        
        points.append(data[y][x])
        visited.append((y * width) + x)
        
        self.flood_fill_util(data, x + 1, y, points, visited, width, height)
        self.flood_fill_util(data, x - 1, y, points, visited, width, height)
        self.flood_fill_util(data, x, y + 1, points, visited, width, height)
        self.flood_fill_util(data, x, y - 1, points, visited, width, height)
    
    def part2(self):
        d = [[int(y) for y in list(x)] for x in self.data]
        
        basins = []
        visited = []
        height = len(d)
        width = len(d[0])
        
        lowest = self.get_lowest_points(d)
        for y, x in lowest:
            points = []
            self.flood_fill_util(d, x, y, points, visited, width, height)
            
            if len(points) > 0:
                basins.append(points)
        
        basins = sorted(basins, key=len, reverse=True)
        a = len(basins[0])
        b = len(basins[1])
        c = len(basins[2])
        
        return a * b * c


Day().solve()
