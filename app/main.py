class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"
    
    def __add__(self, other):
        if isinstance(other, Distance):
           self.km += other.km
        elif isinstance(other, (int, float)):
           self.km += Distance(other).km
        return self
    
    def __iadd__(self, other: None) -> None:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += Distance(other).km
        return self
        
    def __mul__(self, other:float) -> float:
        self.km *= other
        return self
    
    def __truediv__(self, other: float) -> float:
        self.km = round(self.km / other, 2)
        return self
    
    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < Distance(other).km

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > Distance(other).km

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == Distance(other).km

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= Distance(other).km

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= Distance(other).km
