class Distance:
    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        return Distance(other + self.km)

    def __iadd__(self, other):
        if isinstance(other, (int, float)) is True:
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, other):
        return Distance(round(self.km / other, 2))

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

    def __len__(self):
        return self
