from common.solution import Solution


class Day(Solution):
    def execute(self, start, d):
        def get_val(x):
            return int(x) if x.isdigit() else self.execute(x, d)

        if isinstance(d[start], int):
            return d[start]
        length = len(d[start])

        if length == 1:
            d[start] = get_val(d[start][0])

        elif length == 2:
            op, right = d[start]
            v = (~get_val(right)) & 0xFFFF
            d[start] = v

        elif length == 3:
            left, op, right = d[start]
            v = -1
            match op:
                case "OR":
                    v = get_val(left) | get_val(right)
                case "AND":
                    v = get_val(left) & get_val(right)
                case "LSHIFT":
                    v = get_val(left) << int(right)
                case "RSHIFT":
                    v = get_val(left) >> int(right)
            d[start] = v

        return d[start]

    def part1(self):
        d = {}
        for line in self.data:
            raw_data, wire = line.split(" -> ")
            d[wire] = raw_data.split()

        self.execute("a", d)

        return d["a"]

    def part2(self):
        d = {}
        for line in self.data:
            raw_data, wire = line.split(" -> ")
            d[wire] = raw_data.split()

        # Override wire b with part1's result
        d["b"] = self.part1()  # or store part1 result in self.part1_result

        self.execute("a", d)
        return d["a"]


Day().solve()
