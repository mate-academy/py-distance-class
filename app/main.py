type KM = int | float


class Distance:
    def __init__(self, km: KM) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: KM) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: KM) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, multiplier: KM) -> "Distance":
        return Distance(self.km * multiplier)

    def __truediv__(self, other: KM) -> "Distance":
        if isinstance(other, (int, float)) and other > 0:
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __eq__(self, other: float | int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __lt__(self, other: float | int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __le__(self, other: float | int) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __gt__(self, other: float | int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __ge__(self, other: float | int) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
