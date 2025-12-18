from common.solution import Solution
from string import ascii_letters


class Day(Solution):
    def part1(self):
        alphabet = list(ascii_letters)
        total = 0
        
        for line in self.data:
            first = line[: len(line) // 2]
            second = line[len(line) // 2 :]
            
            first_set = set(first)
            second_set = set(second)
            
            common = first_set & second_set
            
            for item in common:
                total += alphabet.index(item) + 1
        
        return total
    
    def part2(self):
        # TODO: Need part2.py to convert
        pass


Day().solve()
