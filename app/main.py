class Distance:
    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Distance(km = self.km + other)
        elif isinstance(other, Distance):
            return Distance(km = self.km + other.km)

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Distance(km = self.km * other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Distance(km=round(self.km / other, 2))

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            if self.km < other:
                return True
        elif isinstance(other, Distance):
            if self.km < other.km:
                return True
        return False

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            if self.km > other:
                return True
        elif isinstance(other, Distance):
            if self.km > other.km:
                return True
        return False

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            if self.km == other:
                return True
        elif isinstance(other, Distance):
            if self.km == other.km:
                return True
        return False

    def __le__(self, other):
        if isinstance(other, (int, float)):
            if self.km <= other:
                return True
        elif isinstance(other, Distance):
            if self.km <= other.km:
                return True
        return False

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            if self.km >= other:
                return True
        elif isinstance(other, Distance):
            if self.km >= other.km:
                return True
        return False