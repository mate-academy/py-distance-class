class Distance:
    def __init__(self, km: int):
        self.km = km
    def __repr__(self):
        return f"Distance(km={self.km})"
    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __add__(self, other):
        return Distance(
            km=self.km + other.km
        )

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, int):
            self.km += other
            return self

    def __mul__(self, other):
        if isinstance(other, Distance):
            self.km *= other.km
            return self
        elif isinstance(other, int):
            self.km *= other
            return self

    def __truediv__(self, other):
        if isinstance(other, Distance):
            self.km = round(self.km / other.km, 2)
            return self, 2
        elif isinstance(other, int):
            self.km = round(self.km / other, 2)
            return self

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int):
            return self.km < other

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, int):
            return self.km > other

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int):
            return self.km == other

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km != other.km
        elif isinstance(other, int):
            return self.km != other

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, int):
            return self.km >= other
