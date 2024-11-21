class Distance:

    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, addition):
        if isinstance(addition, (int , float)):
            return Distance(self.km + addition)
        if isinstance(addition, Distance):
            return Distance(self.km + addition.km)

    def __iadd__(self, addition):
        if isinstance(addition, (int, float)):
            self.km += addition
            return self
        if isinstance(addition, Distance):
            self.km += addition.km
            return self

    def __mul__(self, multiplier):
        if isinstance(multiplier, (int, float)):
            return Distance(self.km * multiplier)
        if isinstance(multiplier, Distance):
            return Distance(self.km * multiplier.km)

    def __truediv__(self, digit):
        result = round(self.km / digit, 2)
        return Distance(result)

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.km < other
        if isinstance(other, Distance):
            return self.km < other.km

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.km > other
        if isinstance(other, Distance):
            return self.km > other.km

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.km == other
        if isinstance(other, Distance):
            return self.km == other.km

    def __le__(self, other):
        if isinstance(other, (int, float)):
            return self.km <= other
        if isinstance(other, Distance):
            return self.km <= other.km

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return self.km >= other
        if isinstance(other, Distance):
            return self.km >= other.km

    def __len__(self):
        return len(self.km)
