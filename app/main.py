class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        length = self.km + other.km
        return Distance(length)

    def __iadd__(self, other: "Distance") -> "Distance":
        self.km += other.km
        return self

    def __mul__(self, num: int) -> "Distance":
        length = self.km * num
        return Distance(length)

    def __truediv__(self, num: int) -> "Distance":
        length = round(self.km / num, 2)
        return Distance(length)

    def __lt__(self, other: "Distance") -> bool:
        return self.km < other.km

    def __gt__(self, other: "Distance") -> bool:
        return self.km > other.km

    def __eq__(self, other: "Distance") -> bool:
        return self.km == other.km

    def __le__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km

    def __ge__(self, other: "Distance") -> bool:
        return self.km >= other.km
