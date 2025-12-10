from linereader import read_file
from lib.point3d import Point3D

points = [Point3D(*map(int, x.split(','))) for x in read_file('input.txt')]
seen_pairs = set()
circuits = [] 

def add_to_circuit(a, b):
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


def run():
    smallest_distance = float('inf')
    smallest_pair = None

    for a in points:
        for b in points:
            if a == b:
                continue

            pair = frozenset([a,b])
            if pair not in seen_pairs:
                distance = a.distance_to(b)
                if distance < smallest_distance:
                    smallest_distance = distance
                    smallest_pair = pair
    
    if smallest_pair is not None:
        seen_pairs.add(smallest_pair)
        
        # Unpack frozenset to get a and b
        a, b = smallest_pair
        add_to_circuit(a, b)

def simulate(runs):
    for _ in range(runs):
        run()

distances = []
for i, a in enumerate(points):
    for b in points[i+1:]:  # Only check pairs once
        d = a.distance_to(b)
        distances.append((d, a, b))

# Sort by distance
distances.sort()

for i in range(1000):
    _, a, b = distances[i]
    add_to_circuit(a, b)
#Get the three largest circuits by length
circuit_sizes = sorted([len(c) for c in circuits], reverse=True)
result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]

print(result)