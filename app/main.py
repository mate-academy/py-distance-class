class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            total = self.km + other
        else:
            total = self.km + other.km
        return Distance(total)

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            total = self.km * other
        else:
            total = self.km * other.km
        return Distance(total)

    def __truediv__(self, other):
        total = round(self.km / other, 2)
        return Distance(total)

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.km < other
        else:
            return self.km < other.km

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.km > other
        else:
            return self.km > other.km

    def __le__(self, other):
        if isinstance(other, (int, float)):
            return self.km <= other
        else:
            return self.km <= other.km

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return self.km >= other
        else:
            return self.km >= other.km

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.km == other
        else:
            return self.km == other.km

    def __len__(self):
        return self.km
