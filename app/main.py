class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        return Distance(self.km + other.km) if \
            isinstance(other, Distance) else \
            Distance(self.km + Distance(other).km)

    def __iadd__(self, other):
        self.km = self.km + other.km if \
            isinstance(other, Distance) else \
            self.km + Distance(other).km
        return self

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, operand):
        other = round((self.km / operand), 2)
        return Distance(other)

    def __lt__(self, other):
        return self.km < Distance(other).km

    def __gt__(self, other):
        return self.km > Distance(other).km

    def __ge__(self, other):
        return self.km >= Distance(other).km

    def __le__(self, other):
        return self.km <= Distance(other).km

    def __eq__(self, other):
        return self.km == Distance(other).km

    def __len__(self):
        return self.km
