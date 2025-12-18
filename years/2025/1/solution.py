from common.solution import Solution


class Day(Solution):
    def parse_input(self, raw: str):
        return [x for x in raw.strip().split("\n")]

    def part1(self):
        cur_index = 50
        count = 0
        for item in self.data:
            direction = item[0]
            steps = int(item[1:])

            if direction == "L":
                cur_index = (cur_index - steps) % 100
            elif direction == "R":
                cur_index = (cur_index + steps) % 100

            if cur_index == 0:
                count += 1

        return count

    def part2(self):
        cur_index = 50
        count = 0

        for item in self.data:
            direction = item[0]
            steps = int(item[1:])

            if direction == "L":
                if cur_index == 0:
                    count += steps // 100
                elif steps >= cur_index:
                    count += 1 + (steps - cur_index) // 100
                cur_index = (cur_index - steps) % 100
            elif direction == "R":
                if cur_index == 0:
                    count += steps // 100
                elif steps >= 100 - cur_index:
                    count += 1 + (steps - (100 - cur_index)) // 100
                cur_index = (cur_index + steps) % 100

        return count


Day().solve()
