from common.solution import Solution
import re

p1_pattern = re.compile(
    r"^(?!.*(?:ab|cd|pq|xy))"   
    r"(?=(?:.*[aeiou]){3,})"   
    r".*(.)\1"                 
)

class Day(Solution):
    def is_nice(self, line):
        pairs = {}
        has_pair_twice = False
        has_repeat_with_gap = False

        for i in range(len(line)):
            if i + 2 < len(line):
                if line[i] == line[i + 2]:
                    has_repeat_with_gap = True

            if i + 1 < len(line):
                pair = line[i:i + 2]

                if pair not in pairs:
                    pairs[pair] = i
                else:
                    if i >= pairs[pair] + 2:
                        has_pair_twice = True

            if has_pair_twice and has_repeat_with_gap:
                return True

        return False

    def part1(self):
        count = 0
        
        for line in self.data:
            if bool(p1_pattern.search(line)):
                count += 1
        return count
        
    def part2(self):
        count = 0
        
        for line in self.data:
            if(self.is_nice(line)):
                count +=1
        
        return count


Day("input.txt").solve()
