class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f'Distance: {self.km} kilometers.'

    def __repr__(self):
        return f'Distance(km={self.km})'

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float) is True:
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(self, other):
        if isinstance(other, int) or isinstance(other, float) is True:
            self.km = self.km + other
            return self
        else:
            self.km = self.km + other.km
            return self

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, other):
        return Distance(round(self.km / other, 2))

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, float) is True:
            if self.km < other:
                return True
            return False
        else:
            if self.km < other.km:
                return True
            return False

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, float) is True:
            if self.km > other:
                return True
            return False
        else:
            if self.km > other.km:
                return True
            return False

    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, float) is True:
            if self.km == other:
                return True
            return False
        else:
            if self.km == other.km:
                return True
            return False

    def __le__(self, other):
        if isinstance(other, int) or isinstance(other, float) is True:
            if self.km <= other:
                return True
            return False
        else:
            if self.km <= other.km:
                return True
            return False

    def __ge__(self, other):
        if isinstance(other, int) or isinstance(other, float) is True:
            if self.km >= other:
                return True
            return False
        else:
            if self.km >= other.km:
                return True
            return False

    def __len__(self):
        return self.km
