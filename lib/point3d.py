import math


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))
    
    def __repr__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"
    
    def distance_to(self, other):
        """Calculate Euclidean distance to another point."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
    
    def manhattan_distance_to(self, other):
        """Calculate Manhattan distance to another point."""
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

