class Distance:
    def __init__(self, km):
        self.km = km

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __add__(self, other):
        return Distance(
            km=(self.km + other.km)
            if isinstance(other, Distance)
            else self.km + other
        )

    def __iadd__(self, other):
        self.km = (self.km + other.km) \
            if isinstance(other, Distance) \
            else self.km + other
        return self

    def __mul__(self, number):
        return Distance(self.km * number)

    def __truediv__(self, number):
        return Distance(round(self.km / number, 2))

    def __lt__(self, other):
        return self.km < other.km \
            if isinstance(other, Distance) \
            else self.km < other

    def __gt__(self, other):
        return self.km > other.km \
            if isinstance(other, Distance) \
            else self.km > other

    def __eq__(self, other):
        return self.km == other.km \
            if isinstance(other, Distance) \
            else self.km == other

    def __le__(self, other):
        return self.km <= other.km \
            if isinstance(other, Distance) \
            else self.km <= other

    def __ge__(self, other):
        return self.km >= other.km \
            if isinstance(other, Distance) \
            else self.km >= other

    def __len__(self):
        return self.km
