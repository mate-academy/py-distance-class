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
        return Distance(km=other + self.km)

    def __iadd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = other
            self.km += result
        else:
            result = other.km
            self.km += result
        return self

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, other):
        return Distance(round(self.km / other, 2))

    def __lt__(self, other):
        return self.km < other

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other):
        return self.km == other

    def __le__(self, other):
        return self.km <= other

    def __ge__(self, other):
        return self.km >= other
