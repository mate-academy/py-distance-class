class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, int):
            return Distance(self.km + other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, int):
            self.km += other
            return self

    def __mul__(self, number):
        return Distance(self.km * number)

    def __truediv__(self, number):
        return Distance(round(self.km / number, 2))

    def __lt__(self, other):
        if isinstance(other, Distance):
            return True if self.km < other.km else False
        if isinstance(other, int):
            return True if self.km < other else False

    def __gt__(self, other):
        if isinstance(other, Distance):
            return True if self.km > other.km else False
        if isinstance(other, int):
            return True if self.km > other else False

    def __eq__(self, other):
        if isinstance(other, Distance):
            return True if self.km == other.km else False
        if isinstance(other, int):
            return True if self.km == other else False

    def __le__(self, other):
        if isinstance(other, Distance):
            return True if self.km <= other.km else False
        if isinstance(other, int):
            return True if self.km <= other else False

    def __ge__(self, other):
        if isinstance(other, Distance):
            return True if self.km >= other.km else False
        if isinstance(other, int):
            return True if self.km >= other else False

    def __len__(self):
        return self.km
