from common.solution import Solution
from itertools import permutations, cycle
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from computer import Computer


class Day(Solution):
    def parse_input(self, raw: str):
        return [int(x) for x in raw.strip().split(',')]
    
    def part1(self):
        ans = 0
        phase_set = permutations(range(5), 5)

        for phase_settings in phase_set:
            output = 0
            for phase in phase_settings:
                output = Computer(self.data.copy()).run([phase, output])
            ans = max(ans, output)

        return ans
    
    def part2(self):
        ans = 0
        phase_set = list(permutations(range(5, 10), 5))

        for phase in phase_set:
            amplifiers = [Computer(self.data.copy(), [phase[i]]) for i in range(5)]
            amp_iter = cycle(amplifiers)

            output = 0
            while not amplifiers[4].halted:
                output = next(amp_iter).run([output])

            ans = max(ans, output)

        return ans


Day().solve()
