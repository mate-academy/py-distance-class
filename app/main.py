class Distance:
    def __init__(self, km):
        self.km = km
    
    def __str__(self):
        return f"{self.km} km"
    
    def __repr__(self):
        return f"Distance(km={self.km})"
    
    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented