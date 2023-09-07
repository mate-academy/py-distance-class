class Distance:

    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers"

    def __repr__(self):
        return f"Distance({self.km} km)"

    def __add__(self, other):
        if isinstance(other, Distance):
            sum_km = self.km + other.km
            return Distance(sum_km)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self

    def __mul__(self, other):
        if isinstance(other, int):
            return Distance(self.km * other)
    pass
