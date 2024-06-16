class Distance:
    def __init__(self, km: float = 0.0):
        self.km = km

    def __str__(self):
        return f"Distance is - {self.km} kilometers"

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance) is False:
            raise TypeError("Wrong instance, try again")
        return Distance(self.km + other.km)

    def __iadd__(self, other):
        self.km = self.km + other.km
        return self.km

    def __mul__(self, other):
        return Distance(self.km * other.km)

    def __truediv__(self, other):
        return Distance(round(self.km / other.km, 2))

    def __lt__(self, other):
        return Distance(self.km + other.km > other.km + self.km)

    def __gt__(self, other):
        return Distance(self.km > other.km)

    def __eq__(self, other):
        return Distance(self.km == other.km)

    def __le__(self, other):
        return Distance(self.km <= other.km)

    def __ge__(self, other):
        return Distance(self.km >= other.km)


distance1 = Distance(km=20)
distance2 = Distance(km=30)









