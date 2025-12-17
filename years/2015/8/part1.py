from common.solution import Solution


class Day(Solution):
    def encode(self, line):
        escaped = line.replace("\\", "\\\\").replace('"', '\\"')
        return '"' + escaped + '"'

    def part1(self):
        total = 0
        for line in self.data:
            literal_length = len(line)
            memory_length = len(eval(line))
            diff = literal_length - memory_length
            total += diff

        return total

    def part2(self):
        total = 0

        for line in self.data:
            literal_length = len(line)
            encoded_length = len(self.encode(line))
            diff = encoded_length - literal_length
            total += diff

        return total


Day().solve()
