from common.solution import Solution
from lib.point3d import Point3D


class Day(Solution):
    def parse_input(self, raw: str):
        return [Point3D(*map(int, x.split(','))) for x in raw.strip().split('\n')]
    
    def add_to_circuit(self, a, b, circuits):
        """Add connection between points a and b to circuits"""
        a_circuit = None
        b_circuit = None
        for circuit in circuits:
            if a in circuit:
                a_circuit = circuit
            if b in circuit:
                b_circuit = circuit

        # Case 1: Both in same circuit - do nothing
        if a_circuit is not None and a_circuit is b_circuit:
            pass  # Already connected

        # Case 2: a in c1, b in c2 - merge circuits
        elif a_circuit is not None and b_circuit is not None:
            a_circuit.update(b_circuit)
            circuits.remove(b_circuit)

        # Case 3: Only one in a circuit - add the other
        elif a_circuit is not None:
            a_circuit.add(b)
        elif b_circuit is not None:
            b_circuit.add(a)

        # Case 4: Neither in any circuit - create new one
        else:
            circuits.append({a, b})
    
    def part1(self):
        """Find product of three largest circuit sizes after 1000 closest connections"""
        points = self.data
        circuits = []
        
        # Compute all pairwise distances
        distances = []
        for i, a in enumerate(points):
            for b in points[i+1:]:  # Only check pairs once
                d = a.distance_to(b)
                distances.append((d, a, b))

        # Sort by distance
        distances.sort()

        # Connect the 1000 closest pairs
        for i in range(1000):
            _, a, b = distances[i]
            self.add_to_circuit(a, b, circuits)
        
        # Get the three largest circuits by length
        circuit_sizes = sorted([len(c) for c in circuits], reverse=True)
        result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]

        return result
    
    def part2(self):
        """Find first connection that creates a circuit with all points"""
        points = self.data
        circuits = []
        
        # Compute all pairwise distances
        distances = []
        for i, a in enumerate(points):
            for b in points[i+1:]: 
                d = a.distance_to(b)
                distances.append((d, a, b))
                
        distances.sort()

        result = 0
        for _, a, b in distances:
            self.add_to_circuit(a, b, circuits)
            
            if any(len(circuit) == len(points) for circuit in circuits):
                result = a.x * b.x
                break
        
        return result


Day().solve()
