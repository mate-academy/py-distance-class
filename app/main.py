class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if not isinstance(other, Distance):
            result = self.km + other
        else:
            result = self.km + other.km
        return Distance(result)

    def __iadd__(self, other):
        if not isinstance(other, Distance):
            self.km = self.km + other
        else:
            self.km = self.km + other.km
        return self

    def __mul__(self, other):
        result = self.km * other
        return Distance(result)

    def __truediv__(self, other):
        result = self.km / other
        return Distance(round(result, 2))

    def __lt__(self, other):
        if not isinstance(other, Distance):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other):
        if not isinstance(other, Distance):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other):
        if not isinstance(other, Distance):
            return self.km == other
        return self.km == other.km

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __len__(self):
        return self.km
