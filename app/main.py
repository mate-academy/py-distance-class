class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> object:
        if not isinstance(other, Distance):
            other = Distance(other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: object) -> None:
        if not isinstance(other, Distance):
            other = Distance(other)
        self.km = self.km + other.km
        return self

    def __mul__(self, other: int) -> None:
        if isinstance(other, Distance):
            return None
        self.km = self.km * other
        return Distance(self.km)

    def __truediv__(self, other: int) -> None:
        if isinstance(other, Distance):
            return None
        self.km = round(self.km / other, 2)
        return Distance(self.km)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km < other.km

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km > other.km

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km == other.km

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km <= other.km

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km >= other.km
