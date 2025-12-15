from common.solution import Solution
import hashlib


class Day(Solution):
    def simulate(self, start):
        key = self.raw_input.strip()

        number = 0

        while True:
            # Create MD5 hash
            hash_input = f"{key}{number}"
            md5_hash = hashlib.md5(hash_input.encode()).hexdigest()
            if md5_hash.startswith(start):
                return number
            number += 1

    def part1(self):
        return self.simulate("00000")

        
    
    def part2(self):
        return self.simulate("000000")


Day().solve()
