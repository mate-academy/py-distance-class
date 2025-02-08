class Distance:
    @staticmethod
    def check_is_instance(other):
        return isinstance(other, Distance)

    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if self.check_is_instance(other):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other):
        if self.check_is_instance(other):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, other):
        self.km = round(self.km / other, 2)
        return self

    def __lt__(self, other):
        return self.km < other

    def __gt__(self, other):
        return self.km > other

    def __eq__(self, other):
        return self.km == other

    def __le__(self, other):
        return self.km <= other

    def __ge__(self, other):
        return self.km >= other
