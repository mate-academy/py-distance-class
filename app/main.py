class Distance:
    def __init__(self, km):
        if not isinstance(km, (int, float)):
            raise TypeError("km must be a number")
        if km < 0:
            raise ValueError("Distance cannot be negative")
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    # Операторы сравнения
    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented

    # Арифметические операторы
    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __sub__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km - other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km - other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, divisor):
        if not isinstance(divisor, (int, float)):
            raise TypeError("Can only divide by a number")
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Distance(round(self.km / divisor, 2))