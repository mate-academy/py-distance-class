class Distance:
    def __init__(self, km: float = 0.0):
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"  # "Distance(km=20)"

    def __add__(self, other) -> "Distance":
        if not isinstance(other, Distance):
            raise TypeError("both variants ^ are possible")
        return Distance(self.km + other.km)

    def __iadd__(self, other) -> "Distance":
        if not isinstance(other, Distance):
            raise TypeError("both variants ^ are possible")
        self.km += other.km
        return self
    
    def __mul__(self, factor: float) -> "Distance":
        if not isinstance(factor, (int, float)):
            raise TypeError("can only multiply by a number")
        return Distance(self.km * factor)
    
    def __truediv__(self, divisor: float) -> "Distance":
        if not isinstance(divisor, (int, float)):
            raise TypeError("can only divide by a number or float")
        if divisor == 0:
            raise ValueError("cannot divide bt zero")
        return Distance(round(self.km / divisor), 2)
        
    def __lt__(self, other) -> bool:
        if not isinstance(other, Distance):
            raise TypeError("can only compare with another Distance")
        return self.km < other.km

    def __gt__(self, other) -> bool:
        if not isinstance(other, Distance):
            raise TypeError("can only compare with another Distance")
        return self.km > other.km

    def __eq__(self, other) -> bool:
        if not isinstance(other, Distance):
            raise TypeError("can only compare with another Distance")
        return self.km == other.km

    def __le__(self, other) -> bool:
        if not isinstance(other, Distance):
            raise TypeError("can only compare with another Distance")
        return self.km <= other.km

    def __ge__(self, other) -> bool:
        if not isinstance(other, Distance):
            raise TypeError("can only compare with another Distance")
        return self.km >= other.km
        
