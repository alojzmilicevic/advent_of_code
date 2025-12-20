from common.solution import Solution
import re

pattern = re.compile(r"-?\d+")


class Day(Solution):
    def combinations_sum_to(self, total, num_vars):
        if num_vars == 1:
            return [(total,)]

        result = []
        for i in range(total + 1):
            for combo in self.combinations_sum_to(total - i, num_vars - 1):
                result.append((i,) + combo)

        return result

    def part1(self):
        total = 0
        n = len(self.data)

        for combination in self.combinations_sum_to(100, n):
            cap = 0
            dur = 0
            flav = 0
            tex = 0

            for comb in combination:
                print(comb, end=" ")
            print()

        # self.data is list of lines, self.raw_input is the raw string
        return None

    def part2(self):
        return None


Day(test=True).solve()
