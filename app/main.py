class Distance:

    def __init__(self, km):
        self.km = km

    def __add__(self, other):
        if type(other) is Distance:
            return Distance(self.km + other.km)
        elif type(other) is int:
            return Distance(self.km + other)

    def __iadd__(self, other):
        if type(other) is Distance:
            self.km += other.km
        elif type(other) is int:
            self.km += other
        return self

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, other):
        return Distance(round(self.km / other, 2))

    def __lt__(self, other):
        if type(other) is Distance:
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other):
        if type(other) is Distance:
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other):
        if type(other) is Distance:
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __len__(self):
        return self.km

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __str__(self):
        return f"Distance: {self.km} kilometers."
