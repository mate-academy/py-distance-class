class Distance:

    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers"

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        else:
            return Distance(km=self.km + other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, mul):
        return Distance(km=self.km * mul)

    def __truediv__(self, dev):
        return Distance(km=round(self.km / dev, 2))

    def __lt__(self, other):
        if isinstance(other, Distance):
            return True if self.km < other.km else False
        else:
            return True if self.km < other else False

    def __gt__(self, other):
        if isinstance(other, Distance):
            return True if self.km > other.km else False
        else:
            return True if self.km > other else False

    def __eq__(self, other):
        if isinstance(other, Distance):
            return True if self.km == other.km else False
        else:
            return True if self.km == other else False

    def __le__(self, other):
        if isinstance(other, Distance):
            return True if self.km <= other.km else False
        else:
            return True if self.km <= other else False

    def __ge__(self, other):
        if isinstance(other, Distance):
            return True if self.km >= other.km else False
        else:
            return True if self.km >= other else False

    def __len__(self):
        return len(range(self.km))
