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


distances = []
for i, a in enumerate(points):
    for b in points[i+1:]: 
        d = a.distance_to(b)
        distances.append((d, a, b))
        
distances.sort()

result = 0
for _, a, b in distances:
    add_to_circuit(a, b)
    
    if any(len(circuit) == len(points) for circuit in circuits):
        result = a.x * b.x
        break
print(result)