class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, (float, int)):
            return Distance(self.km + other)
        elif isinstance(other, Distance):
            return Distance(self.km + other.km)

    def __iadd__(self, other):
        if isinstance(other, (float, int)):
            self.km += other
            return self
        self.km += other.km
        return self

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Distance(self.km * other)
        return Distance(self.km * other.km)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return None

    def __lt__(self, other):
        if isinstance(other, (float, int)):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other):
        if isinstance(other, (float, int)):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other):
        if isinstance(other, (float, int)):
            return self.km == other
        return self.km == other.km

    def __le__(self, other):
        if isinstance(other, (float, int)):
            return not self > other
        return not self > other.km

    def __ge__(self, other):
        if isinstance(other, (float, int)):
            return not self < other
        return not self < other

    def __len__(self):
        return self.km
