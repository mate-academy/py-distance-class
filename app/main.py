class Distance:
    def __init__(self, km):
        self.km = km

    def __add__(self, other):
        return Distance(other + self.km)

    def __iadd__(self, other):
        self.km = other + self.km
        return self

    def __len__(self):
        return self.km

    def __repr__(self):
        return 'Distance(km={})'.format(self.km)

    def __mul__(self, other):
        return Distance(self.km * other)

    def __str__(self):
        return 'Distance: {} kilometers'.format(self.km)

    def __truediv__(self, other):
        return Distance(round(self.km / other, 2))

    def __eq__(self, other):
        return self.km == other

    def __lt__(self, other):
        return self.km < other

    def __gt__(self, other):
        return self.km > other

    def __le__(self, other):
        return self.km <= other

    def __ge__(self, other):
        return self.km >= other
