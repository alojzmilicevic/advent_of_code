from common.solution import Solution


class Day(Solution):
    def part1(self):
        arr = []
        for i in range(len(self.data)):
            if i == 0:
                for item in self.data[i]:
                    arr.append([0, 0])
            
            line = self.data[i]
            
            for k in range(len(line)):
                arr[k][int(line[k])] += 1
        
        gamma = ''
        epsilon = ''
        for item in arr:
            if item[0] > item[1]:
                gamma += "0"
                epsilon += "1"
            else:
                gamma += "1"
                epsilon += "0"
        
        return int(gamma, 2) * int(epsilon, 2)
    
    def part2(self):
        data = [int(x, 2) for x in self.data]
        bits = max(x.bit_length() for x in data)
        
        o2, co2 = [*data], [*data]
        for i in range(bits - 1, -1, -1):
            o2_bit = sum((x >> i) & 1 for x in o2) >= len(o2) / 2
            o2 = [x for x in o2 if (x >> i) & 1 == o2_bit] or o2
        
        for i in range(bits - 1, -1, -1):
            co2_bit = sum((x >> i) & 1 for x in co2) < len(co2) / 2
            co2 = [x for x in co2 if (x >> i) & 1 == co2_bit] or co2
        
        return o2[0] * co2[0]


Day().solve()
