class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(km=other.km + self.km)
        else:
            return Distance(km=other + self.km)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, other):
        return Distance(round((self.km / other), 2))

    def __lt__(self, other):
        return self.km < other.km if isinstance(other, Distance) \
            else self.km < other

    def __gt__(self, other):
        return self.km > other.km \
            if isinstance(other, Distance) else self.km > other

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other):
        return self.km <= other.km \
            if isinstance(other, Distance) else self.km <= other

    def __ge__(self, other):
        return self.km >= other.km \
            if isinstance(other, Distance) else self.km >= other

    def __len__(self):
        return len("0" * self.km)
