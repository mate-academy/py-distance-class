class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"

    def __add__(self, other: float) -> None:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: float) -> None:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, num: float) -> float:
        return Distance(self.km * num)

    def __truediv__(self, divisor: int) -> None:
        result_km = self.km / divisor
        return Distance(round(result_km, 2))

    def __lt__(self, other: float) -> float:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: float) -> float:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: float) -> float:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: float) -> float:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: float) -> float:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
