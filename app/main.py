class Distance:

    def __init__(self, km):
        self.km = km

    def __str__(self):
        print(f"Distance: {self.km} kilometers")

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        return Distance(
            km=self.km + other
        )

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other):
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other):
        return Distance(
            km=round(self.km / other, 2)
        )

    def __eq__(self, other):
        return self.km == other

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other

    def __gt__(self, other):
        return not self == other and not self < other

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __len__(self):
        return self.km
