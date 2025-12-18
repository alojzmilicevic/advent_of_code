from common.solution import Solution
import sys
import heapq


class Day(Solution):
    def is_valid(self, x, y, height, width):
        return 0 <= x < width and 0 <= y < height
    
    def dijkstra(self, grid):
        pq = [(0, (0, 0))]
        ROWS = len(grid)
        COLS = len(grid[0])
        
        distances = [[sys.maxsize for col in line] for line in grid]
        
        # Left, Above, Right, below
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        distances[0][0] = grid[0][0]
        
        while pq:
            dist, (i, j) = heapq.heappop(pq)
            
            if i == ROWS - 1 and j == COLS - 1:
                return distances[i][j] - grid[0][0]
            
            for k in range(4):
                x = j + dx[k]
                y = i + dy[k]
                
                if self.is_valid(x, y, ROWS, COLS):
                    if distances[y][x] > grid[y][x] + distances[i][j]:
                        heapq.heappush(pq, (distances[i][j] + grid[y][x], (y, x)))
                        distances[y][x] = distances[i][j] + grid[y][x]
        
        return -1
    
    def part1(self):
        d = [[int(y) for y in list(x)] for x in self.data]
        return self.dijkstra(d)
    
    def part2(self):
        d = [[int(y) for y in list(x)] for x in self.data]
        
        new_map = [line * 5 for line in d * 5]
        
        size = len(d)
        for i in range(size * 5):
            for j in range(size * 5):
                new_map[i][j] = (new_map[i][j] + i // size + j // size - 1) % 9 + 1
        
        return self.dijkstra(new_map)


Day().solve()
