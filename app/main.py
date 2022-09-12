class Distance:
    def __init__(self, km: int):
        self.km = km

    @staticmethod
    def instancecheck(other, instance):
        return True if isinstance(other, instance) else False

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if Distance.instancecheck(other, Distance):
            self.km = self.km + other.km
        else:
            self.km = float(self.km) + other
        return self

    def __iadd__(self, other):
        if Distance.instancecheck(other, Distance):
            self.km = self.km + other.km
        else:
            self.km = float(self.km) + other
        return self

    def __mul__(self, other):
        if Distance.instancecheck(other, Distance):
            self.km = self.km * other.km
        else:
            self.km = float(self.km) * other
        return self

    def __truediv__(self, other):
        if other == 0:
            return "Zero division error"
        elif Distance.instancecheck(other, Distance):
            self.km = round(self.km / other, 2)
        else:
            self.km = round(float(self.km) / other, 2)
        return self

    def __lt__(self, other):
        if Distance.instancecheck(other, Distance):
            return self.km < other.km
        return float(self.km) < other

    def __gt__(self, other):
        if Distance.instancecheck(other, Distance):
            return self.km > other.km
        return float(self.km) > other

    def __eq__(self, other):
        if Distance.instancecheck(other, Distance):
            return self.km == other.km
        return float(self.km) == other

    def __le__(self, other):
        if Distance.instancecheck(other, Distance):
            return self.km <= other.km
        return float(self.km) <= other

    def __ge__(self, other):
        if Distance.instancecheck(other, Distance):
            return self.km >= other.km
        return float(self.km) >= other

    def __len__(self):
        return self.km
