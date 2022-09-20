class Distance:

    def __init__(self, km: float):
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
        else:
            self.km += other
        #
        return self

    def __mul__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km * other.km)
        return Distance(self.km * other)

    def __truediv__(self, other):
        if isinstance(other, Distance):
            return Distance(round(self.km / other.km, 2))
        return Distance(round(self.km / other, 2))

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __lt__(self, other):
        return not self.__eq__(other) and not self.__gt__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __len__(self):
        return self.km
