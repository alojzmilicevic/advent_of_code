from common.solution import Solution


class Day(Solution):
    def part1(self):
        elf_calories = []
        cur_cal = 0
        for i in range(len(self.data)):
            if self.data[i] == "":
                elf_calories.append(cur_cal)
                cur_cal = 0
            else:
                cal = int(self.data[i])
                cur_cal += cal
        
        return max(elf_calories)
    
    def part2(self):
        elf_calories = []
        cur_cal = 0
        for i in range(len(self.data)):
            if self.data[i] == "":
                elf_calories.append(cur_cal)
                cur_cal = 0
            else:
                cal = int(self.data[i])
                cur_cal += cal
        
        sorted_elf_calories = sorted(elf_calories, reverse=True)
        return sorted_elf_calories[0] + sorted_elf_calories[1] + sorted_elf_calories[2]


Day().solve()
