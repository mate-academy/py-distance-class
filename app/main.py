class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float) -> float:
        if isinstance(other, Distance) is True:
            return Distance(km=self.km + other.km)
        else:
            return Distance(km=self.km + other)

    def __iadd__(self, other: float) -> float:
        if isinstance(other, Distance) is True:
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, other: float) -> float:
        return Distance(km=self.km * other)

    def __truediv__(self, other: float) -> float:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: float) -> float:
        return self.km < other

    def __gt__(self, other: float) -> float:
        return self.km > other

    def __eq__(self, other: float) -> float:
        return self.km == other

    def __le__(self, other: float) -> float:
        return self.km <= other

    def __ge__(self, other: float) -> float:
        return self.km >= other
