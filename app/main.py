class Distance:

    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: object) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: object) -> "Distance":
        result = self.km / other
        return Distance(round(result, 2))

    def __lt__(self, other: object) -> bool:
        return self.km < other

    def __gt__(self, other: object) -> bool:
        return self.km > other

    def __eq__(self, other: object) -> bool:
        return self.km == other

    def __le__(self, other: object) -> bool:
        return self.km <= other

    def __ge__(self, other: object) -> bool:
        return self.km >= other
