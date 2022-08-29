class Distance:

    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        if isinstance(other, (int, float)):
            return Distance(
                km=self.km + other
            )

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (float, int)):
            self.km += other
            return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Distance(
                km=self.km * other
            )
        if isinstance(other, Distance):
            return Distance(
                km=self.km * other.km
            )

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Distance(
                km=round(self.km / other, 2)
            )
        if isinstance(other, Distance):
            return Distance(
                km=round(self.km / other.km, 2)
            )

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (float, int)):
            return self.km < other

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (float, int)):
            return self.km > other

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (float, int)):
            return self.km == other

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (float, int)):
            return self.km <= other

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (float, int)):
            return self.km >= other

    def __len__(self):
        return self.km
