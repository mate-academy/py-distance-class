class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {str(self.km)} kilometers."

    def __repr__(self):
        return f"Distance(km={str(self.km)})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, int):
            return Distance(self.km + other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km = self.km + other.km
        elif isinstance(other, int):
            self.km = self.km + other
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            return Distance(self.km * other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return Distance(round(self.km / other, 2))

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int):
            return self.km < other

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, int):
            return self.km > other

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int):
            return self.km == other

    def __len__(self):
        return self.km


print(Distance(50) > Distance(50))
