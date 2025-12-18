from common.solution import Solution


class Day(Solution):
    def run_checker(self, points, part2):
        matching_pairs = {
            "{": "}",
            "[": "]",
            "(": ")",
            "<": ">",
        }
        
        points_map = {
            ")": points[0],
            "]": points[1],
            "}": points[2],
            ">": points[3],
        }
        
        total = 0
        scores = []
        
        for a in self.data:
            stack = []
            error = False
            cur_p = 0
            for i in range(len(a)):
                c = a[i]
                if c == '[' or c == '(' or c == '{' or c == '<':
                    stack.append((c, i))
                else:
                    if not stack:
                        continue
                    opening_type = stack.pop()
                    if c != matching_pairs[opening_type[0]]:
                        total += points_map[c]
                        error = True
                        break
            
            if not error and part2:
                for item in reversed(stack):
                    cur_p = (cur_p * 5) + points_map[matching_pairs[item[0]]]
                scores.append(cur_p)
        
        return scores, total
    
    def part1(self):
        points_1 = [3, 57, 1197, 25137]
        res = self.run_checker(points_1, False)
        return res[1]
    
    def part2(self):
        points_2 = [1, 2, 3, 4]
        res = self.run_checker(points_2, True)
        scores = res[0]
        return sorted(scores)[len(scores) // 2]


Day().solve()
