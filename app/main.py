class Distance:
    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if type(other) == int:
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(self, other):
        if type(other) == int:
            self.km += other
            return self
        else:
            self.km += other.km
            return self

    def __mul__(self, other):
        if type(other) == int:
            return Distance(self.km * other)
        else:
            return Distance(self.km * other.km)

    def __truediv__(self, other):
        if type(other) == int:
            return Distance(round(self.km / other, 2))
        else:
            return Distance(round(self.km / other.km, 2))

    def __eq__(self, other):
        if type(other) == int:
            return self.km == other
        else:
            return self.km == other.km

    def __gt__(self, other):
        if type(other) == int:
            return self.km > other
        else:
            return self.km > other.km

    def __lt__(self, other):
        if type(other) == int:
            return self.km < other
        else:
            return self.km < other.km

    def __ge__(self, other):
        if type(other) == int:
            return self.km >= other
        else:
            return self.km >= other.km

    def __le__(self, other):
        if type(other) == int:
            return self.km <= other
        else:
            return self.km <= other.km

    def __len__(self):
        return self.km
