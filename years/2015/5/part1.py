from common.solution import Solution
import re

vowels_pattern = re.compile("[aeiou]")
twice_in_a_row_pattern = re.compile(r"(.)\1")
forbidden_patterns = ["ab", "cd", "pq", "xy"]

class Day(Solution):
    def has_three_vowels(self, line):
        return len(vowels_pattern.findall(line)) >= 3
    
    def has_double_letter(self, line):
        return bool(twice_in_a_row_pattern.search(line))
    
    def has_no_forbidden_patterns(self, line):
        for pattern in forbidden_patterns:
            if pattern in line:
                return False
        return True
    
    def has_letter_pair_twice(self, line):
        None
    
    def has_repeat_with_one_between(self, line):
        None
    
    def part1(self):
        count = 0
        
        for line in self.data:
            if (self.has_three_vowels(line) and
                self.has_double_letter(line) and
                self.has_no_forbidden_patterns(line)):
                count += 1
        return count
        
    def part2(self):
        count = 0
        
        for line in self.data:
            if(self.has_letter_pair_twice(line) and 
               self.has_repeat_with_one_between(line)):
                count +=1
        
        return count


Day().solve()
