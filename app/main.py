class Distance:
    def __init__(self, km: float):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance({self.km})"

    def __add__(self, other: object) -> object:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return NotImplemented

    def __mul__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero.")
            return Distance(self.km / other)
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return NotImplemented

    def __le__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return NotImplemented

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return NotImplemented
