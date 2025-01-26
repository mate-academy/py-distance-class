class Distance:
    def __init__(self, km):
        if not isinstance(km, (int, float)):
            raise ValueError("km must be a number.")
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
        else:
            raise ValueError("Can only add Distance or numeric values.")

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise ValueError("Can only add Distance or numeric values.")
        return self

    def __mul__(self, factor):
        if not isinstance(factor, (int, float)):
            raise ValueError("Can only multiply by a numeric value.")
        return Distance(self.km * factor)

    def __truediv__(self, divisor):
        if not isinstance(divisor, (int, float)) or divisor == 0:
            raise ValueError("Divisor must be a non-zero numeric value.")
        return Distance(round(self.km / divisor, 2))

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise ValueError("Comparison is only supported with Distance or numeric values.")

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise ValueError("Comparison is only supported with Distance or numeric values.")

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise ValueError("Comparison is only supported with Distance or numeric values.")

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise ValueError("Comparison is only supported with Distance or numeric values.")
