from common.solution import Solution


class Day(Solution):
    def parse_input(self, raw: str):
        return [int(x) for x in raw.strip().split("\n")]

    def part1(self):
        start = self.data[0]
        total = 0
        for item in self.data:
            if item > start:
                total += 1
            start = item
        return total

    def part2(self):
        start = self.data[0] + self.data[1] + self.data[2]
        total = 0
        for i in range(1, len(self.data) - 2):
            cur = self.data[i] + self.data[i + 1] + self.data[i + 2]
            if cur > start:
                total += 1
            start = cur
        return total


Day().solve()
