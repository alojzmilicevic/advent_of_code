from common.solution import Solution


class Day(Solution):
    def calculate_floor(self, target=None):
        total = 0
        for i, char in enumerate(self.raw_input):
            if char == '(':
                total += 1
            elif char == ')':
                total -= 1
            
            if target is not None and total == target:
                return i + 1
        return total
    
    def part1(self):
        return self.calculate_floor()
    
    def part2(self):
        return self.calculate_floor(target=-1)


Day().solve()
