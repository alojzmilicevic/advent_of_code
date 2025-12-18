from common.solution import Solution
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from computer import Computer


class Day(Solution):
    def parse_input(self, raw: str):
        return [int(x) for x in raw.strip().split(',')]
    
    def part1(self):
        c = Computer(self.data.copy())
        for i in range(9):
            if i == 0:
                c.run([1, 1])
            else:
                c.run([1])
        return c.run([1])
    
    def part2(self):
        c = Computer(self.data.copy())
        c.run([5, 1])
        return c.run([1])


Day().solve()
