class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(
                km=self.km + other,
            )
        elif isinstance(other, Distance):
            return Distance(
                km=self.km + other.km,
            )
        raise TypeError

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        else:
            raise TypeError
        return self

    def __mul__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(
                km=self.km * other
            )
        raise TypeError

    def __truediv__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(
                km=round(self.km / other, 2),
            )
        raise TypeError

    def __lt__(self, other: "Distance") -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km
        raise TypeError

    def __gt__(self, other: "Distance") -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km
        raise TypeError

    def __eq__(self, other: "Distance") -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        elif isinstance(other, Distance):
            return self.km == other.km
        raise TypeError

    def __le__(self, other: "Distance") -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        elif isinstance(other, Distance):
            return self.km <= other.km
        raise TypeError

    def __ge__(self, other: "Distance") -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        elif isinstance(other, Distance):
            return self.km >= other.km
        raise TypeError

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"
