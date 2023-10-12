class Distance:
    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return "Distance(km=" + str(self.km) + ")"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, other):
        return Distance(round((self.km / other), 2))

    def __lt__(self, other):
        if isinstance(other, Distance):
            if self.km < other.km:
                return True
        else:
            if self.km < other:
                return True
        return False

    def __gt__(self, other):
        if isinstance(other, Distance):
            if self.km > other.km:
                return True
        else:
            if self.km > other:
                return True
        return False

    def __eq__(self, other):
        if isinstance(other, Distance):
            if self.km == other.km:
                return True
        else:
            if self.km == other:
                return True
        return False

    def __le__(self, other):
        if isinstance(other, Distance):
            if self.km <= other.km:
                return True
        else:
            if self.km <= other:
                return True
        return False

    def __ge__(self, other):
        if isinstance(other, Distance):
            if self.km >= other.km:
                return True
        else:
            if self.km >= other:
                return True
        return False
