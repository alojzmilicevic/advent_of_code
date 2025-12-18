from common.solution import Solution
import re


class Day(Solution):
    def execute(self, line):
        result = ""

        groups = [m.group() for m in re.finditer(r"(.)\1*", line)]

        for group in groups:
            result += str(len(group)) + group[0]

        return result

    def part1(self):
        line = self.raw_input
        for _ in range(40):
            line = self.execute(line)
        return len(line)

    def part2(self):
        line = self.raw_input
        for _ in range(50):
            line = self.execute(line)
        return len(line)


Day().solve()
