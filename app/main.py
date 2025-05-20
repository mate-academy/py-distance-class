class Distance:

    def __init__(self, km):
        self.km = km

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other

    def __mul__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km * other.km)
        else:
            return Distance(self.km * other)

    def __truediv__(self, other):
        if isinstance(other, Distance):
            return Distance(round(self.km / other.km, 2))
        else:
            return Distance(round(self.km / other.km, 2))

    def __lt__(self, other):
        return self.km < other.km

    def __gt__(self, other):
        return self.km > other.km

    def __eq__(self, other):
        return self.km == other.km

    def __le__(self, other):
        return self.km <= other.km

    def __ge__(self, other):
        return self.km >= other.km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"{self.__class__.__name__}(km={self.km})"