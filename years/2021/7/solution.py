from common.solution import Solution
from statistics import median


class Day(Solution):
    def part1(self):
        data = [int(x) for x in self.data[0].split(',')]
        med = int(median(data))
        
        total_distance = 0
        for item in data:
            total_distance += abs(item - med)
        
        return total_distance
    
    def get_cost(self, a, b):
        n = abs(a - b)
        return (n * (n + 1)) // 2
    
    def part2(self):
        data = [int(x) for x in self.data[0].split(',')]
        
        costs = []
        for pos in range(min(data), max(data)):
            costs.append(sum(self.get_cost(i, pos) for i in data))
        
        return min(costs)


Day().solve()
