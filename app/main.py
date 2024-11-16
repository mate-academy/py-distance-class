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

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Distance(km=self.km * factor)

    def __truediv__(self, divisor):
        if isinstance(divisor, (int, float)) and divisor != 0:
            return Distance(km=self.km / divisor)

