class Distance:
    def __init__(self, km: float) -> float:
        self.km = km

    def __str__(self: Distance) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self: Distance) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            return NotImplemented

    def __iadd__(self, other: Distance) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        else:
            return NotImplemented
        return self

    def __mul__(self, other: Distance) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: Distance) -> Distance:
        if not isinstance(other, (int, float)):
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError("division by zero")
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        if isinstance(other, Distance):
            return self.km == other.km
        return NotImplemented

    def __lt__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        if isinstance(other, Distance):
            return self.km < other.km
        return NotImplemented

    def __le__(self, other: Distance) -> bool:
        return self == other or self < other

    def __gt__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        if isinstance(other, Distance):
            return NotImplemented

    def __ge__(self, other: Distance) -> bool:
        eq = self == other
        if eq is NotImplemented:
            return NotImplemented
        gt = self > other
        if gt is NotImplemented:
            return NotImplemented
        return eq or gt
