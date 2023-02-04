class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        number = isinstance(other, int) or isinstance(other, float)
        if number:
            self.km = self.km + other.real
        else:
            self.km = self.km + other.km
        return self

    def __iadd__(self, other):
        number = isinstance(other, int) or isinstance(other, float)
        if number:
            self.km += other.real
            return self
        self.km += other.km
        return self

    def __mul__(self, other):
        self.km = self.km * other.real
        return self

    def __truediv__(self, other):
        self.km = self.km / other.real
        return Distance(round(self.km, 2))

    def __lt__(self, other):
        number = isinstance(other, int) or isinstance(other, float)
        if number:
            return self.km < other.real
        return self.km < other.km

    def __gt__(self, other):
        number = isinstance(other, int) or isinstance(other, float)
        if number:
            return self.km > other.real
        return self.km > other.km

    def __eq__(self, other):
        number = isinstance(other, int) or isinstance(other, float)
        if number:
            return self.km == other.real
        return self.km == other.km

    def __le__(self, other):
        number = isinstance(other, int) or isinstance(other, float)
        if number:
            return self.km <= other.real
        return self.km <= other.km

    def __ge__(self, other):
        number = isinstance(other, int) or isinstance(other, float)
        if number:
            return self.km >= other.real
        return self.km >= other.km

    def __len__(self):
        return self.km
