class Distance:
    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        raise TypeError("Operand must be of type 'Distance'")

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        raise TypeError("Operand must be of type 'Distance'")

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Distance(km=self.km * factor)
        raise TypeError("Factor must be a number (int or float)")

    def __truediv__(self, divisor):
        if isinstance(divisor, (int, float)) and divisor != 0:
            return Distance(km=round(self.km / divisor, 2))
        if divisor == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        raise TypeError("Divisor must be a number (int or float)")

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        raise TypeError("Operand must be of type 'Distance'")

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        raise TypeError("Operand must be of type 'Distance'")

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        raise TypeError("Operand must be of type 'Distance'")

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        raise TypeError("Operand must be of type 'Distance'")

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        raise TypeError("Operand must be of type 'Distance'")


