class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self):
        return f"Distance: {self.km:.2f} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported operand type for +")

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.km += other
            return self
        elif isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            raise TypeError("Unsupported operand type for +=")

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            result = self.km / other
            return Distance(round(result, 2))
        else:
            raise TypeError("Unsupported operand type for /")

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
