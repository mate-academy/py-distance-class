class Distance:
    def __init__(self, km: int):
        self.km = km

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __str__(self):
        return f"Distance: {self.km} kilometers"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (float, int)):
            return Distance(self.km + other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (float, int)):
            self.km += other
        return self

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, other):
        return Distance(round(self.km / other, 2))

    def __lt__(self, other):
        if isinstance(other, (float, int, Distance)):
            return True if self.km < other else False

    def __gt__(self, other):
        if isinstance(other, (float, int, Distance)):
            return True if self.km > other else False

    def __eq__(self, other):
        if isinstance(other, (float, int, Distance)):
            return True if self.km == other else False

    def __le__(self, other):
        if isinstance(other, (float, int, Distance)):
            return True if self.km <= other else False

    def __ge__(self, other):
        if isinstance(other, (float, int, Distance)):
            return True if self.km >= other else False

    def __len__(self):
        return self.km
