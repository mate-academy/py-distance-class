class Distance:
    def __init__(self, km: float) -> float:
        self.km = km

    def __str__(self) -> float:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> float:
        return f"Distance(km={self.km})"

    def __add__(self, other: float) -> float:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: float) -> float:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, factor: float) -> float:
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)
        return NotImplemented

    def __truediv__(self, divisor: float) -> float:
        if isinstance(divisor, (int, float)) and divisor != 0:
            return Distance(round(self.km / divisor, 2))
        return NotImplemented

    def __lt__(self, other: float) -> float:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: float) -> float:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __eq__(self, other: float) -> float:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented

    def __le__(self, other: float) -> float:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: float) -> float:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented
