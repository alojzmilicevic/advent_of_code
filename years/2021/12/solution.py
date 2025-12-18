from common.solution import Solution


class Day(Solution):
    def create_graph(self, lines):
        pairs = [tuple(line.split('-')) for line in lines]
        
        verticies = list(set([node for tup in pairs for node in tup]))
        graph = dict().fromkeys(verticies, [])
        
        for src, dest in pairs:
            if dest not in graph[src] and dest != 'start':
                graph[src] = [*graph[src], dest]
            if src not in graph[dest] and src != 'start':
                graph[dest] = [*graph[dest], src]
        
        return graph
    
    def find_paths(self, graph, vertex, visited, flag=False):
        visited.append(vertex)
        if vertex == 'end':
            return [visited]
        
        paths = []
        for neighbour in graph[vertex]:
            if neighbour not in visited or neighbour.isupper():
                new_paths = self.find_paths(graph, neighbour, visited.copy(), flag)
                paths.extend(new_paths)
            elif neighbour.islower() and flag:
                new_paths = self.find_paths(graph, neighbour, visited.copy(), False)
                paths.extend(new_paths)
        return paths
    
    def part1(self):
        g = self.create_graph(self.data)
        p = self.find_paths(g, 'start', [], False)
        return len(p)
    
    def part2(self):
        g = self.create_graph(self.data)
        p = self.find_paths(g, 'start', [], True)
        return len(p)


Day().solve()
