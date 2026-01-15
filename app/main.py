class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, n) -> "Distance":
        return Distance(self.km * n)

    def __truediv__(self, other) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other) -> bool:  # "less than"
        other_km = other.km if isinstance(other, Distance) else other
        return self.km < other_km

    def __gt__(self, other) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km > other_km

    def __eq__(self, other) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km == other_km

    def __le__(self, other) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km <= other_km

    def __ge__(self, other) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km >= other_km
