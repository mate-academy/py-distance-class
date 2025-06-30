class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        return Distance(self.km + other.km)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            self.km *= other
        else:
            self.km *= other
        return self

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            self.km = round(self.km / other, 2)
        else:
            self.km = round(self.km / other, 2)
        return self
