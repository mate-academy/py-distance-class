class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, number):
        if isinstance(number, (int, float)):
            self.km += number
            return self
        self.km = self.km + number.km
        return self

    def __mul__(self, number):
        return Distance(self.km * number)

    def __truediv__(self, number):
        return Distance(round(self.km / number, 2))

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km

    def __le__(self, other):
        if isinstance(other, (int, float)):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return self.km >= other
        return self.km >= other.km
