class Distance:
    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if not isinstance(other, Distance):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other):
        if not isinstance(other, Distance):
            self.km += other
            return self
        self.km += other.km
        return self

    def __mul__(self, other):
        self.km = self.km * other
        return self

    def __truediv__(self, other):
        self.km = round(self.km / other, 2)
        return self

    def __eq__(self, other):
        if not isinstance(other, Distance):
            return self.km == other
        return self.km == other.km

    def __gt__(self, other):
        if not isinstance(other, Distance):
            return self.km > other
        return self.km > other.km

    def __ge__(self, other):
        if not isinstance(other, Distance):
            return self.km >= other
        return self.km >= other.km

    def __lt__(self, other):
        if not isinstance(other, Distance):
            return self.km < other
        return self.km < other.km

    def __le__(self, other):
        if not isinstance(other, Distance):
            return self.km <= other
        return self.km <= other.km
