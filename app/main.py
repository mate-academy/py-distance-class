class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(other.km + self.km)
        else:
            return Distance(other + self.km)

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km = other + self.km
            return self

    def __str__(self) -> str:
        return "Distance: {0} kilometers.".format(self.km)

    def __repr__(self) -> str:
        return "Distance(km={0})".format(self.km)

    def __mul__(self, other: float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(other * self.km)

    def __truediv__(self, other: float) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
