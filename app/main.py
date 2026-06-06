class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> int:
        distance1 = self.km

        if isinstance(other, Distance):
            distance2 = other.km
            distance3 = distance1 + distance2
        else:
            distance3 = distance1 + other

        return Distance(distance3)

    def __iadd__(self, other: int) -> Distance:

        if isinstance(other, Distance):
            self.km = self.km + other.km
        else:
            self.km = self.km + other

        return self

    def __mul__(self, other: int) -> Distance:
        distance1 = self.km
        distance3 = distance1 * other

        return Distance(distance3)

    def __truediv__(self, other: int) -> Distance:
        distance1 = self.km
        distance3 = distance1 / other
        distance3 = round(distance3, 2)

        return Distance(distance3)

    def __lt__(self, other: int) -> bool:
        distance1 = self.km

        if isinstance(other, Distance):
            distance2 = other.km
            distance3 = distance1 < distance2
        else:
            distance3 = distance1 < other

        return bool(distance3)

    def __gt__(self, other: int) -> bool:
        distance1 = self.km

        if isinstance(other, Distance):
            distance2 = other.km
            distance3 = distance1 > distance2
        else:
            distance3 = distance1 > other

        return bool(distance3)

    def __eq__(self, other: int) -> bool:
        distance1 = self.km

        if isinstance(other, Distance):
            distance2 = other.km
            distance3 = distance1 == distance2
        else:
            distance3 = distance1 == other

        return bool(distance3)

    def __le__(self, other: int) -> bool:
        distance1 = self.km

        if isinstance(other, Distance):
            distance2 = other.km
            distance3 = distance1 <= distance2
        else:
            distance3 = distance1 <= other

        return bool(distance3)

    def __ge__(self, other: int) -> bool:
        distance1 = self.km

        if isinstance(other, Distance):
            distance2 = other.km
            distance3 = distance1 >= distance2
        else:
            distance3 = distance1 >= other

        return bool(distance3)
