class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, int | float):
            distance2 = self.km + other
            return Distance(distance2)
        else:
            distance3 = self.km + other.km
            return Distance(distance3)

    def __iadd__(self, other):
        if isinstance(other, int | float):
            self.km += other
            return self
        else:
            self.km += other.km
            return self

    def __mul__(self, other):
        distance2 = self.km * other
        return Distance(distance2)

    def __truediv__(self, other):
        distance2 = self.km / other
        return Distance(round(distance2, 2))

    def __lt__(self, other):
        return self.km < other

    def __gt__(self, other):
        return self.km > other

    def __eq__(self, other):
        return self.km == other

    def __le__(self, other):
        return self.km <= other

    def __ge__(self, other):
        return self.km >= other
