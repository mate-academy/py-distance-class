class Distance:
    def __init__(self, km: int or float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km!r})"

    def __add__(self, other: int or "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(
                self.km + other
            )
        return Distance(
            self.km + other.km
        )

    def __iadd__(self, other: int or "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other: int) -> "Distance":
        self.km *= other
        return self

    def __truediv__(self, other: int) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int or "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: int or "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: int or "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: int or "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: int or "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
