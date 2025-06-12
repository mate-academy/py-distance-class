class Distance:
    
    def __init__(self, distance):
        self.distance = distance

    def __str__(self):
        return f'("Distance: {self.distance} kilometers.")'

    def __repr__(self):
        return f"Distance(km={self.distance})"
    
    def __add__(self, other):
        return Distance(self.distance + other.distance)

    def __iadd__(self, other):
        self.distance = self.distance + other.distance
        return self.distance
    
    def __mul__(self, other):
        if isinstance(other, Distance):
            return Distance(self.distance * other.distance)

    def __truediv__(self, other):
        if isinstance(other, Distance):
            if other.distance == 0:
                raise ZeroDivisionError("Division by zero")
            return Distance(self.distance / other.distance) 

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.distance < other.distance

    
    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.distance > other.distance
    
    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.distance == other.distance
        return False
    
    def __le__(self, other):
        if isinstance(other, Distance):
            return self.distance <= other.distance
    
    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.distance >= other.distance
        
