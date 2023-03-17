class Distance:
    # Write your code here
    def __init__(self, km: int) -> None:
        self.km = km  # distance.km == 20

    def __str__(self):
        return f"Distance: {self.km} kilometers."  # "Distance: 20 kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"  # "Distance(km=20)"

    def __add__(self, other: int) -> __class__:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self, other: int) -> __class__:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int) -> __class__:
        return Distance(self.km * other)
    # isinstance(distance2, Distance) is True
    # distance2.km == 100

    def __truediv__(self, other: int) -> __class__:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int) -> __class__:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: int) -> __class__:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: int) -> __class__:
        return self.km == other

    def __le__(self, other: int) -> __class__:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: int) -> __class__:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
