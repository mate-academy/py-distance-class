class Distance:

    def __init__(self, km):
        self.km = km

    def __str__(self):
        return 'Distance: ' + str(self.km) + ' kilometers.'

    def __repr__(self):
        return 'Distance(km=' + str(self.km) + ')'

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
        return Distance(round(self.km / other, 2))

    def __lt__(self, other):
        if isinstance(other, int):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other):
        if isinstance(other, int):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other):
        if isinstance(other, int):
            return self.km == other
        return self.km == other.km

    def __le__(self, other):
        if isinstance(other, int):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other):
        if isinstance(other, int):
            return self.km >= other
        return self.km >= other.km

    def __len__(self):
        return self.km
