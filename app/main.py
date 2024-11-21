class Distance:

    def __init__(self, km):
        self.km = km

    # representation functions

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __len__(self):
        return self.km

    # math functions

    def __add__(self, other):
        return Distance(
            self.km + other.km if isinstance(other, Distance)
            else self.km + other
        )

    def __iadd__(self, other):
        self.km = self.km + other.km if isinstance(other, Distance) \
            else self.km + other
        return self

    def __mul__(self, other):
        return Distance(
            self.km * other
        )

    def __truediv__(self, other):
        return Distance(
            round(self.km / other, 2)
        )

    # comparison functions

    def __lt__(self, other):
        return self.km < other.km if isinstance(other, Distance) \
            else self.km < other

    def __gt__(self, other):
        return self.km > other.km if isinstance(other, Distance) \
            else self.km > other

    def __eq__(self, other):
        return self.km == other.km if isinstance(other, Distance) \
            else self.km == other

    def __le__(self, other):
        return self.km <= other.km if isinstance(other, Distance) \
            else self.km <= other

    def __ge__(self, other):
        return self.km >= other.km if isinstance(other, Distance) \
            else self.km >= other
