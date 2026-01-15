class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers"

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | float | int") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: "Distance | float | int") -> "Distance":
        if isinstance(other, Distance):
            self.km += other
        else:
            self.km += other.km
        return f"{self.km} is {self}"

    def __mul__(self, other: int | float) -> "Distance":
        return self.km * other.km

    def __truediv__(self, other: int | float) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: "Distance") -> bool:
        return self.km < other.km

    def __gt__(self, other: "Distance") -> bool:
        return self.km > other.km

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            return False
        return self.km == other.km

    def __le__(self, other: "Distance") -> bool:
        return self.km <= other.km

    def __ge__(self, other: "Distance") -> bool:
        return self.km >= other.km

