from common.solution import Solution


class Day(Solution):
    def delta(self, t1, t0):
        if t1 == t0:
            return 0
        return int((t1 - t0) / abs(t1 - t0))
    
    def calc(self, diag):
        lines = [x.strip().split(" -> ") for x in self.data]
        lines = [[x.split(",") for x in p] for p in lines]
        
        mapper = {}
        for f, t in lines:
            x0, y0, x1, y1 = *map(int, f), *map(int, t)
            if not diag and x0 != x1 and y0 != y1:
                continue
            while x0 != x1 or y0 != y1:
                mapper[(x0, y0)] = mapper.get((x0, y0), 0) + 1
                x0 += self.delta(x1, x0)
                y0 += self.delta(y1, y0)
            mapper[(x0, y0)] = mapper.get((x0, y0), 0) + 1
        return sum((1 for d in mapper.values() if d > 1))
    
    def part1(self):
        return self.calc(False)
    
    def part2(self):
        return self.calc(True)


Day().solve()
