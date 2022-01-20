class Distance:

    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)

        return Distance(self.km + other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Distance(round(self.km * other, 2))
        else:
            raise TypeError(f"{type(other)} can`t be multiply on {type(self.km)}")

    def __truediv__(self, other):
        result = self.km / other
        return Distance(float(f"{result:.{2}f}"))

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other

    def __len__(self):
        return self.km


person = Distance(20)
pre = Distance(30)
r = person * pre
print(r)
