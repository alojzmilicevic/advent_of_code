from pprint import pprint
from common.solution import Solution
import re
import json


class Day(Solution):
    def part1(self):
        data = re.findall(r"-?\d+", self.data[0])
        total = 0
        for num in data:
            total += int(num)
        return total

    def part2(self):
        data = json.loads(self.data[0])

        def sum_without_red(obj):
            if isinstance(obj, dict):
                if "red" in obj.values():
                    return 0
                return sum(sum_without_red(v) for v in obj.values())
            elif isinstance(obj, list):
                return sum(sum_without_red(item) for item in obj)
            elif isinstance(obj, int):
                return obj
            return 0

        return sum_without_red(data)


Day().solve()
