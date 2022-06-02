class Distance:
    def __init__(self, km):
        self.km = km
        if not isinstance(self.km, (int, float, Distance)):
            raise TypeError(f"Uncorrected type '{self.km}'."
                            f" Must be int, float, {Distance}")

    @staticmethod
    def type_checking(other):
        if type(other) is Distance:
            return other.km
        elif isinstance(other, (int, float)):
            return other
        else:
            raise TypeError(f"Uncorrected type '{other}'."
                            f" Must be int, float, {Distance}")

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        return Distance(self.km + self.type_checking(other))

    def __iadd__(self, other):
        self.km += self.type_checking(other)
        return self

    def __mul__(self, other):
        return Distance(self.km * self.type_checking(other))

    def __truediv__(self, other):
        return Distance(round(self.km / self.type_checking(other), 2))

    def __lt__(self, other):
        return self.km < self.type_checking(other)

    def __gt__(self, other):
        return self.km > self.type_checking(other)

    def __eq__(self, other):
        return self.km == self.type_checking(other)

    def __le__(self, other):
        return self.km <= self.type_checking(other)

    def __ge__(self, other):
        return self.km >= self.type_checking(other)

    def __len__(self):
        return self.km
