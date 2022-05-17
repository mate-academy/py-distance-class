class Distance:
    def __init__(self, km):
        self.km = km

    @staticmethod
    def get_other_km(other):
        return other if isinstance(other, int) else other.km

    def __str__(self):
        return f"Distance: {self.km} kilometers"

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        return Distance(self.km + self.get_other_km(other))

    def __iadd__(self, other):
        self.km += self.get_other_km(other)
        return self

    def __mul__(self, other):
        self.km *= other
        return self

    def __truediv__(self, other):
        self.km = round(self.km / other, 2)
        return self

    def __lt__(self, other):
        return self.km < self.get_other_km(other)

    def __gt__(self, other):
        return self.km > self.get_other_km(other)

    def __eq__(self, other):
        return self.km == self.get_other_km(other)

    def __le__(self, other):
        return self.km <= self.get_other_km(other)

    def __ge__(self, other):
        return self.km >= self.get_other_km(other)

    def __len__(self):
        return self.km
