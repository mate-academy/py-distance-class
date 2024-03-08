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
        elif isinstance(other, int):
            return Distance(self.km + other)
        else:
            raise ValueError("Unsupported type for addition")

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, int):
            self.km += other
        else:
            raise ValueError("Unsupported type for addition")
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            return Distance(self.km * other)
        else:
            raise ValueError("Unsupported type for multiplication")

    def __truediv__(self, other):
        if isinstance(other, int):
            result = self.km / other
            return Distance(round(result, 2))
        else:
            raise ValueError("Unsupported type for division")

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int):
            return self.km < other
        else:
            raise ValueError("Unsupported type for comparison")

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, int):
            return self.km > other
        else:
            raise ValueError("Unsupported type for comparison")

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int):
            return self.km == other
        else:
            raise ValueError("Unsupported type for comparison")

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, int):
            return self.km <= other
        else:
            raise ValueError("Unsupported type for comparison")

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, int):
            return self.km >= other
        else:
            raise ValueError("Unsupported type for comparison")
