import math


class Distance:
    def __init__(self, km: float):
        self.km = km

    def __str__(self):
        return f'Distance: {self.km} kilometers.'

    def __repr__(self):
        return f'Distance(km={self.km})'

    def __add__(self, other):
        if isinstance(other, Distance):
            self.km = self.km + other.km
        elif isinstance(other, (int, float)):
            self.km = self.km + other
        else:
            raise TypeError("Unsupported type for addition")
        return self

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported type for addition")
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            self.km *= other
        else:
            raise TypeError("Unsupported type for multiplication")
        return self

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("Unsupported type for division")

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return False

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return False

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return False

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return False

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return False
