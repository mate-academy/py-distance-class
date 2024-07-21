class Distance:
    # Write your code here
    def __init__(self, km: int) -> None:
        self.km = km

    def __add__(self, other: "Distance") -> "Distance":
        if not isinstance(other, Distance):
            return Distance(km=self.km + other.real)
        return Distance(
            km=self.km + other.km
        )

    def __iadd__(self, other: "Distance") -> "Distance":
        if not isinstance(other, Distance):
            self.km += other.real
        else:
            self.km += other.km
        return self

    def __mul__(self, other: "Distance") -> "Distance":
        if not isinstance(other, Distance):
            return Distance(
                km=self.km * other.real
            )

    def __truediv__(self, other: "Distance") -> "Distance":
        if not isinstance(other, Distance):
            return Distance(
                km=round(self.km / other.real, 2)
            )

    def __lt__(self, other: "Distance") -> bool:
        if not isinstance(other, Distance):
            return self.km < other.real
        return self.km < other.km

    def __gt__(self, other: "Distance") -> bool:
        if not isinstance(other, Distance):
            return self.km > other.real
        return self.km > other.km

    def __eq__(self, other: "Distance") -> bool:
        if not isinstance(other, Distance):
            return self.km == other.real
        return self.km == other.km

    def __le__(self, other: "Distance") -> bool:
        if not isinstance(other, Distance):
            return self.km <= other.real
        return self.km <= other.km

    def __ge__(self, other: "Distance") -> bool:
        if not isinstance(other, Distance):
            return self.km >= other.real
        return self.km >= other.km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."
