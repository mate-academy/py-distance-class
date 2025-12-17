class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float | "Distance") -> "Distance":
        value = other.km if isinstance(other, Distance) else other
        return Distance(self.km + value)

    def __iadd__(self, other: float | "Distance") -> "Distance":
        value = other.km if isinstance(other, Distance) else other
        self.km += value
        return self

    def __mul__(self, other: float) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: float | "Distance") -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km < value

    def __gt__(self, other: float | "Distance") -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km > value

    def __eq__(self, other: float | "Distance") -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km == value

    def __le__(self, other: float | "Distance") -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km <= value

    def __ge__(self, other: float | "Distance") -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km >= value
