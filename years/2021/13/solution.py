from common.solution import Solution


class Day(Solution):
    def parse_fold_input(self):
        # Split into points and instructions
        points_data = []
        instructions_data = []
        
        reading_instructions = False
        for line in self.data:
            if not line.strip():
                reading_instructions = True
                continue
            
            if reading_instructions:
                instructions_data.append(line)
            else:
                points_data.append(line)
        
        # Parse points
        points = [[int(p[0]), int(p[1])] for p in [x.split(',') for x in points_data]]
        
        # Parse instructions
        instructions = [(y[0], int(y[2:])) for y in [x.split('fold along ')[1] for x in instructions_data]]
        
        return points, instructions
    
    def remove_duplicates(self, lst):
        return [[t[0], t[1]] for t in (set(tuple(i) for i in lst))]
    
    def part1(self):
        points, instructions = self.parse_fold_input()
        
        # Do first fold only
        fold = instructions[0]
        plane, position = fold
        
        if plane == 'y':
            for i, point in enumerate(points):
                if point[1] > position:
                    points[i][1] = position - abs(position - point[1])
        else:
            for i, point in enumerate(points):
                if point[0] > position:
                    points[i][0] = position - abs(position - point[0])
        
        points = self.remove_duplicates(points)
        
        return len(points)
    
    def part2(self):
        points, instructions = self.parse_fold_input()
        
        # Do all folds
        for fold in instructions:
            plane, position = fold
            
            if plane == 'y':
                for i, point in enumerate(points):
                    if point[1] > position:
                        points[i][1] = position - abs(position - point[1])
            else:
                for i, point in enumerate(points):
                    if point[0] > position:
                        points[i][0] = position - abs(position - point[0])
            
            points = self.remove_duplicates(points)
        
        # Print the pattern
        x_max = max(p[0] for p in points)
        y_max = max(p[1] for p in points)
        
        mat = []
        for row in range(y_max + 1):
            vec = []
            for col in range(x_max + 1):
                vec.append(' ')
            mat.append(vec)
        
        for p in points:
            mat[p[1]][p[0]] = '#'
        
        result = '\n'
        for row in mat:
            result += ''.join(row) + '\n'
        
        return result


Day().solve()
