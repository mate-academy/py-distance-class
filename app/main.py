class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError(
            f"Unsupported operand type(s): "
            f"Distance and {type(other)}"
        )

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        if isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km * other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError(
            f"Unsupported operand type(s): "
            f"Distance and {type(other.km)}"
        )

    def __truediv__(self, other):
        if isinstance(other, Distance):
            return Distance(round(self.km / other.km, 2))
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        raise TypeError(
            f"Unsupported operand type(s): "
            f"Distance and {type(other.km)}"
        )

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other

    def __len__(self):
        return len(self.km)
