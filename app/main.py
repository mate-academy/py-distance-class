class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            km = self.km + other.km
        else:
            km = self.km + other
        return Distance(km)

    def __iadd__(self, other):
        self.km = self.__add__(other).km
        return self

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, other):
        return Distance(round(self.km / other, 2))

    def __lt__(self, other):
        km = other.km if isinstance(other, Distance) else other
        return self.km < km

    def __gt__(self, other):
        km = other.km if isinstance(other, Distance) else other
        return self.km > km

    def __eq__(self, other):
        km = other.km if isinstance(other, Distance) else other
        return self.km == km

    def __le__(self, other):
        km = other.km if isinstance(other, Distance) else other
        return self.km <= km

    def __ge__(self, other):
        km = other.km if isinstance(other, Distance) else other
        return self.km >= km

    def __len__(self):
        return self.km
