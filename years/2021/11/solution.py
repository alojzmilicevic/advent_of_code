from common.solution import Solution
import queue


class Day(Solution):
    def get_neighbours(self, row, col, size):
        arr = [
            (row - 1, col - 1),
            (row - 1, col),
            (row - 1, col + 1),
            (row, col - 1),
            (row, col + 1),
            (row + 1, col - 1),
            (row + 1, col),
            (row + 1, col + 1)
        ]
        
        return list(filter(lambda coords: (0 <= coords[0] < size) and 0 <= coords[1] < size, arr))
    
    def sim(self, d, q):
        f = 0
        size = len(d)
        
        def first_pass():
            fl = 0
            for row in range(len(d)):
                for col in range(len(d[row])):
                    d[row][col] += 1
                    
                    if d[row][col] > 9:
                        q.put((row, col))
                        d[row][col] = 0
                        fl += 1
            
            return fl
        
        f += first_pass()
        
        while not q.empty():
            current = q.get()
            neighbours = self.get_neighbours(current[0], current[1], size)
            
            for neighbour, (y, x) in enumerate(neighbours):
                if d[y][x] != 0:
                    d[y][x] += 1
                
                if d[y][x] > 9:
                    q.put((y, x))
                    d[y][x] = 0
                    f += 1
        return f
    
    def part1(self):
        d = [[int(y) for y in list(x)] for x in self.data]
        q = queue.Queue()
        
        flashes = 0
        for i in range(100):
            flashes += self.sim(d, q)
        
        return flashes
    
    def part2(self):
        d = [[int(y) for y in list(x)] for x in self.data]
        q = queue.Queue()
        
        for i in range(1000):
            self.sim(d, q)
            if sum(sum(d, [])) == 0:
                return i + 1
        
        return 0


Day().solve()
