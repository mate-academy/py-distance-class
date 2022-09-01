class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        return Distance(
            self.km + other.real if isinstance(other, (int, float))
            else self.km + other.km
        )

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.km += other.real
        else:
            self.km += other.km
        return self

    def __mul__(self, other):
        return Distance(
            self.km * other.real if isinstance(other, (int, float))
            else self.km * other.km
        )

    def __truediv__(self, other):
        return Distance(
            round(self.km / other.real, 2) if isinstance(other, (int, float))
            else round(self.km / other.km, 2)
        )

    def __lt__(self, other):
        return self.km < other.real if isinstance(other, (int, float)) \
            else self.km < other.km

    def __gt__(self, other):
        return self.km > other.real if isinstance(other, (int, float)) \
            else self.km > other.km

    def __eq__(self, other):
        return self.km == other.real if isinstance(other, (int, float)) \
            else self.km == other.km

    def __le__(self, other):
        return self.km <= other.real if isinstance(other, (int, float)) \
            else self.km <= other.km

    def __ge__(self, other):
        return self.km >= other.real if isinstance(other, (int, float)) \
            else self.km >= other.km

    def __len__(self):
        return self.km
