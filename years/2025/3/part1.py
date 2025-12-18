from common.solution import Solution


class Day(Solution):
    NUM_BATTERIES = 12

    def parse_input(self, raw: str):
        return [x for x in raw.strip().split("\n")]

    def max_subsequence(self, digits, n):
        """Find the maximum subsequence of length n"""
        digits = list(map(int, digits))
        length = len(digits)
        result = []
        start = 0

        for i in range(n):
            max_index = length - (n - len(result))

            best_digit = -1
            best_pos = start
            for pos in range(start, max_index + 1):
                if digits[pos] > best_digit:
                    best_digit = digits[pos]
                    best_pos = pos
                if best_digit == 9:
                    break

            result.append(str(best_digit))
            start = best_pos + 1

        return "".join(result)

    def part1(self):
        count = 0
        for line in self.data:
            count += int(self.max_subsequence(line, 2))

        return count

    def part2(self):
        count = 0
        for line in self.data:
            count += int(self.max_subsequence(line, self.NUM_BATTERIES))

        return count


Day().solve()
