class Distance:

    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        print(f"Distance: {self.km} kilometers")

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if type(other) == int:
            return Distance(km=self.km + other)
        else:
            return Distance(km=self.km + other.km)

    def __iadd__(self, other):
        if type(other) == int:
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other):
        return Distance(km=self.km * other)

    def __truediv__(self, other):
        return Distance(km=round((self.km / other), 2))

    def __lt__(self, other):
        if type(other) == int:
            return self.km < other
        else:
            return self.km < other.km

    def __gt__(self, other):
        if type(other) == int:
            return self.km > other
        else:
            return self.km > other.km

    def __eq__(self, other):
        if type(other) == int:
            return self.km == other
        else:
            return self.km == other.km

    def __le__(self, other):
        if type(other) == int:
            return self.km <= other
        else:
            return self.km <= other.km

    def __ge__(self, other):
        if type(other) == int:
            return self.km >= other
        else:
            return self.km >= other.km

    def __len__(self):
        return self.km
