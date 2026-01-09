class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if not isinstance(other, Distance):
            return Distance(km=self.km + other.real)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other):
        if not isinstance(other, Distance):
            self.km += other.real
        else:
            self.km += other.km
        return self

    def __lt__(self, other):
        if not isinstance(other, Distance):
            return self.km < other.real
        return self.km < other.km

    def __gt__(self, other):
        if not isinstance(other, Distance):
            return self.km > other.real
        return self.km > other.km

    def __eq__(self, other):
        if not isinstance(other, Distance):
            return self.km == other.real
        return self.km == other.km

    def __le__(self, other):
        if not isinstance(other, Distance):
            return self.km <= other.real
        return self.km <= other.km

    def __ge__(self, other):
        if not isinstance(other, Distance):
            return self.km >= other.real
        return self.km >= other.km

    def __mul__(self, other):
        return Distance(km=self.km * other)

    def __truediv__(self, other):
        return Distance(km=round((self.km / other), 2))
