from common.solution import Solution
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from computer import Computer


class Day(Solution):
    def parse_input(self, raw: str):
        return [int(x) for x in raw.strip().split(",")]

    def part1(self):
        data = self.data.copy()
        data[1] = 12
        data[2] = 2
        c = Computer(data)
        return c.run([0])

    def part2(self):
        for noun in range(100):
            for verb in range(100):
                data = self.data.copy()
                data[1] = noun
                data[2] = verb
                c = Computer(data)
                result = c.run([0])
                if result == 19690720:
                    return 100 * noun + verb
        return None


Day().solve()
