from common.solution import Solution

import re

p1_pattern = re.compile(
    r"^(?=.*(?:abc|bcd|cde|def|efg|fgh|ghi|hjk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz))(?=.*(\w)\1.*(\w)\2)[^iol]+$"
)


class Day(Solution):
    def str_to_num(self, s):
        result = 0
        for char in s:
            result = result * 26 + (ord(char) - ord("a"))
        return result

    def num_to_str(self, num, length):
        result = []
        for _ in range(length):
            result.append(chr(num % 26 + ord("a")))
            num //= 26
        return "".join(reversed(result))

    def increment_string(self, s):
        num = self.str_to_num(s)
        num += 1
        return self.num_to_str(num, len(s))

    def execute(self, start):
        value = start

        while True:
            if bool(p1_pattern.search(value)):
                return value
            value = self.increment_string(value)

    def part1(self):
        start = "hepxcrrq"

        return self.execute(start)

    def part2(self):
        start = self.increment_string(self.part1())

        return self.execute(start)


Day().solve()
