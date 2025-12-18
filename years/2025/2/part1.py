from common.solution import Solution


class Day(Solution):
    def parse_input(self, raw: str):
        lines = raw.strip().split("\n")
        result = []
        for line in lines:
            parts = line.split(",")
            for part in parts:
                result.append(part.strip())
        return result

    def is_even(self, n):
        return len(n) % 2 == 0

    def get_parts(self, s):
        mid = len(s) // 2
        return s[:mid], s[mid:]

    def part1(self):
        count = 0
        for r in self.data:
            parts = r.split("-")
            first = int(parts[0])
            second = int(parts[1])

            for i in range(first, second + 1):
                s = str(i)

                if self.is_even(s):
                    left, right = self.get_parts(s)
                    if left == right:
                        count += i

        return count

    def part2(self):
        count = 0
        for r in self.data:
            parts = r.split("-")
            first = int(parts[0])
            second = int(parts[1])

            for i in range(first, second + 1):
                s = str(i)

                for j in range(1, len(s)):
                    chunks = len(s) // j
                    if chunks > 0 and len(s) % j == 0:
                        all_equal = True
                        first_chunk = s[0:j]
                        for k in range(1, chunks):
                            if s[k * j : (k + 1) * j] != first_chunk:
                                all_equal = False
                                break
                        if all_equal:
                            count += int(s)
                            break

        return count


Day().solve()
