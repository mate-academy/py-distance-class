class Distance:
    def __init__(self, km):
        self.km = km

    @staticmethod
    def check_type(other):
        if isinstance(other, Distance):
            return other.km
        return other

    def __str__(self):
        return f'Distance: {self.km} kilometers.'

    def __repr__(self):
        return f'Distance(km={self.km})'

    def __add__(self, other):
        return Distance(self.km + self.check_type(other))

    def __iadd__(self, other):
        self.km = (self + other).km
        return self

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, other):
        return Distance(round(self.km / other, 2))

    def __lt__(self, other):
        return self.km < self.check_type(other)

    def __gt__(self, other):
        return self.km > self.check_type(other)

    def __eq__(self, other):
        return self.km == self.check_type(other)

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other

    def __len__(self):
        return self.km
