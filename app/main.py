class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        if not isinstance(other, Distance):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance) -> Distance:
        if not isinstance(other, Distance):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: float) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError("Distance can only be multiplied by a number")
        return Distance(self.km * other)

    def __truediv__(self, other: Distance) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError("Distance can only be divided by a number")
        return Distance(round(self.km / other, 2))

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Distance):
            return self.km == value
        else:
            return self.km == value.km

    def __le__(self, other: Distance) -> bool:
        if not isinstance(other, Distance):
            return self.km <= other
        else:
            return self.km <= other.km

    def __ge__(self, other: Distance) -> bool:
        if not isinstance(other, Distance):
            return self.km >= other
        else:
            return self.km >= other.km

    def __gt__(self, other: Distance) -> bool:
        if not isinstance(other, Distance):
            return self.km > other
        else:
            return self.km > other.km

    def __lt__(self, other: Distance) -> bool:
        if not isinstance(other, Distance):
            return self.km < other
        else:
            return self.km < other.km

    def __ne__(self, value: object) -> bool:
        if not isinstance(value, Distance):
            return self.km != value
        else:
            return self.km != value.km
