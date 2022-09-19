class Distance:
    def __init__(self, km: int | float):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        return Distance(self.km + self.instancecheck(other))

    def __iadd__(self, other):
        self.km += self.instancecheck(other)
        return self

    def __mul__(self, other):
        return Distance(self.km * self.instancecheck(other))

    def __truediv__(self, other):
        return Distance(round(self.km / self.instancecheck(other), 2))

    def __lt__(self, other):
        return self.km < self.instancecheck(other)

    def __gt__(self, other):
        return self.km > self.instancecheck(other)

    def __eq__(self, other):
        return self.km == self.instancecheck(other)

    def __le__(self, other):
        return self.km <= self.instancecheck(other)

    def __ge__(self, other):
        return self.km >= self.instancecheck(other)

    def __len__(self):
        return self.km

    @staticmethod
    def instancecheck(other) -> int:
        return other.km if isinstance(other, Distance) else other
