class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers"

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, int):
            return Distance(self.km + other)

        return Distance(self.km + other.km)

    def __iadd__(self, other):
        if isinstance(other, int):
            self.km += other
            return self
        self.km += other.km
        return self

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, other):
        result = self.km / other
        return Distance(round(result, 2))

    def __lt__(self, other):
        if isinstance(other, Distance):
            result = self.km < other.km
        else:
            result = self.km < other
        return result

    def __gt__(self, other):
        if isinstance(other, Distance):
            result = self.km > other.km
        else:
            result = self.km > other
        return result

    def __eq__(self, other):
        if isinstance(other, Distance):
            result = self.km == other.km
        else:
            result = self.km == other
        return result

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other

    def __len__(self):
        return self.km
