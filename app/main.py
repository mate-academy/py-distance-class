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
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError("Unsupported type for addition.")

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported type for addition.")
        return self

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)
        raise TypeError("Unsupported type for multiplication.")

    def __truediv__(self, divisor):
        if isinstance(divisor, (int, float)):
            return Distance(round(self.km / divisor, 2))
        raise TypeError("Unsupported type for division.")

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        raise TypeError("Unsupported type for comparison.")

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return False

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other
