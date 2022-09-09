class Distance:

    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if type(other) == Distance:
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other):
        if type(other) == int or type(other) == float:
            self.km += other
            return self
        else:
            self.km += other.km
            return self

    def __mul__(self, other):
        return Distance(
          self.km * other
        )

    def __truediv__(self, other):
        return Distance(
            round((self.km / other), 2)
        )

    def __eq__(self, other):
        return self.km == other

    def __gt__(self, other):
        return self.km > other

    def __lt__(self, other):
        return self.km < other

    def __ge__(self, other):
        return self.km >= other

    def __le__(self, other):
        return self.km <= other

    def __len__(self):
        return self.km
