class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @classmethod
    def checkvalue(cls, other: "Distance") -> float:
        if not isinstance(other, (int, float, Distance)):
            raise TypeError
        return other if isinstance(other, (int, float)) else other.km

    def __add__(self, other: "Distance") -> "Distance":
        sc = self.checkvalue(other)
        return Distance(self.km + sc)

    def __iadd__(self, other: "Distance") -> "Distance":
        sc = self.checkvalue(other)
        self.km += sc
        return self

    def __mul__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return None

    def __truediv__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)) and other != 0:
            return Distance(round((self.km / other), 2))
        return None

    def __eq__(self, other: "Distance") -> bool:
        sc = self.checkvalue(other)
        return self.km == sc

    def __gt__(self, other: "Distance") -> bool:
        sc = self.checkvalue(other)
        return self.km > sc

    def __ge__(self, other: "Distance") -> bool:
        sc = self.checkvalue(other)
        return self.km >= sc

    def __ne__(self, other: "Distance") -> bool:
        sc = self.checkvalue(other)
        return self.km != sc

    def __lt__(self, other: "Distance") -> bool:
        sc = self.checkvalue(other)
        return self.km < sc

    def __le__(self, other: "Distance") -> bool:
        sc = self.checkvalue(other)
        return self.km <= sc
