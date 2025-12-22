from __future__ import annotations

class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km
    
    def __str__(self: Distance) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self: Distance) -> str:
        return f"Distance(km={self.km})"
    
    def __add__(self: Distance, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
    
    def __iadd__(self: Distance, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self
    
    def __mul__(self: Distance, factor: int | float) -> Distance:
        return Distance(self.km * factor)

    def __truediv__(self: Distance, divisor: int | float) -> Distance:
        rounded_division = round(self.km / divisor, 2)
        return Distance(rounded_division)
    
    def __lt__(self: Distance, other: Distance) -> bool:
        return self.km < other.km
    
    def __gt__(self: Distance, other: Distance) -> bool:
        return self.km > other.km
    
    def __eq__(self: Distance, other: Distance) -> bool:
        return self.km == other.km
    
    def __le__(self: Distance, other: Distance) -> bool:
        return self.km <= other.km
    
    def __ge__(self: Distance, other: Distance) -> bool:
        return self.km >= other.km