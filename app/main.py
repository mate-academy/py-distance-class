class Distance:

    def __init__(self, km):
        self.km = km

    @classmethod
    def verify_data(cls, other):
        if isinstance(other, Distance):
            return other.km
        return other

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        distance = self.verify_data(other)
        return Distance(self.km + distance)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km = self.km + other.km
        elif isinstance(other, (int, float)):
            self.km = self.km + other
        return self

    def __mul__(self, other):
        distance = self.verify_data(other)
        return Distance(self.km * distance)

    def __truediv__(self, other):
        distance = self.verify_data(other)
        return Distance(round(self.km / distance, 2))

    def __eq__(self, other):
        distance = self.verify_data(other)
        return self.km == distance

    def __lt__(self, other):
        distance = self.verify_data(other)
        return self.km < distance

    def __gt__(self, other):
        distance = self.verify_data(other)
        return self.km > distance

    def __le__(self, other):
        distance = self.verify_data(other)
        return self.km <= distance

    def __ge__(self, other):
        distance = self.verify_data(other)
        return self.km >= distance

    def __len__(self, other):
        pass
