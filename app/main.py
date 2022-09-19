class Distance:

    def __init__(self, km) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other):
        return(Distance(km=self.km + other.km)
               if isinstance(other, Distance)
               else Distance(km=self.km + other))

    def __iadd__(self, other):
        self.km = self.km + self.obj_or_int(other)
        return self

    def __mul__(self, mul):
        return Distance(km=self.km * mul)

    def __truediv__(self, div):
        return Distance(km=round((self.km / div), 2))

    def obj_or_int(self, obj):
        return obj.km if isinstance(obj, Distance) else obj

    def __lt__(self, other):
        return self.km < self.obj_or_int(other)

    def __gt__(self, other):
        return self.km > self.obj_or_int(other)

    def __eq__(self, other):
        return self.km == self.obj_or_int(other)

    def __le__(self, other):
        return self.km <= self.obj_or_int(other)

    def __ge__(self, other):
        return self.km >= self.obj_or_int(other)

    def __len__(self):
        return range(self.km)
