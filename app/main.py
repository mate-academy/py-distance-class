class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float) -> isinstance:
        if isinstance(other, Distance):
            res = other.km + self.km
        else:
            res = other + self.km
        return Distance(res)

    def __iadd__(self, other: int) -> isinstance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, other: int) -> isinstance:
        if not isinstance(other, Distance):
            return Distance(self.km * other)

    def __truediv__(self, other: int) -> isinstance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: int) -> bool:
        if isinstance(other, Distance):
            res = self.km == other.km
        else:
            res = self.km == other
        return res

    def __le__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
