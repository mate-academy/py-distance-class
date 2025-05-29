class Distance:
    def __init__(self, km: float):
        self.km = km

    def __str__(self) -> str:
        return  f"Distance: {self.km} kilometers"

    def __repr__(self) -> str:
        return  f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(self, other):
            return Distance(self.km + other.km)
        return Distance(self.km + float(other))

    def __iadd__(self, other):
        if isinstance(self, other):
            self.km += other.km
        else:
            self.km += float(other)
        return self

    def __mul__(self, other):
        return Distance(self.km * float(other))

    def __truediv__(self, other):
        return Distance(round(self.km / float(other), 2))

    def __lt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < float(other)

    def __gt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > float(other)

    def __eq__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == float(other)

    def __le__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= float(other)

    def __ge__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= float(other)
