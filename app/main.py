class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self: Distance) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self: Distance) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)

        return NotImplemented

    def __iadd__(self, other: Distance) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        if isinstance(other, Distance):
            self.km += other.km
            return self
        return NotImplemented

    def __mul__(self, other: Distance) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: Distance | float) -> Distance | float:
        return Distance(round((self.km / other), 2))

    def __lt__(self, other: Distance | float) -> Distance | float:
        if isinstance(other, (int, float)):
            return self.km < other
        if isinstance(other, Distance):
            return self.km < other.km
        return NotImplemented

    def __gt__(self, other: Distance | float) -> Distance | float:
        if isinstance(other, (int, float)):
            return self.km > other
        if isinstance(other, Distance):
            return self.km > other.km
        return NotImplemented

    def __eq__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        if isinstance(other, Distance):
            return self.km == other.km
        return NotImplemented

    def __le__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        if isinstance(other, Distance):
            return self.km <= other.km
        return NotImplemented

    def __ge__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        if isinstance(other, Distance):
            return self.km >= other.km
        return NotImplemented
