class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        elif isinstance(other, Distance):
            return Distance(self.km + other.km)
        return NotImplemented

    def __iadd__(self, other: int) -> "Distance":
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        else:
            return NotImplemented
        return self

    def __mul__(self, other: int) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

        return NotImplemented

    def __truediv__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)) and other != 0:
            return Distance(round(self.km / other, 2))

        return NotImplemented

    def __lt__(self, other: int) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km
        return NotImplemented

    def __gt__(self, other: int) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km
        return NotImplemented

    def __eq__(self, other: int) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        elif isinstance(other, Distance):
            return self.km == other.km
        return NotImplemented

    def __le__(self, other: int) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        elif isinstance(other, Distance):
            return self.km <= other.km
        return NotImplemented

    def __ge__(self, other: int) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        elif isinstance(other, Distance):
            return self.km >= other.km
        return NotImplemented
