class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers"

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other: (Distance, float)) -> Distance:
        if  isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, float):
            return Distance(self.km + other)

    def __iadd__(self, other: (Distance, float)) -> Distance: 
        if  isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, int):
            self.km += other
            return self

    def __mul__(self, other: (float, int)) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: (float, int)) -> Distance:
        return Distance(round((self.km / other), 2))

    def __eq__(self, other: int):
        if  isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int):
            return self.km == other

    def __lt__(self, other: int):
        if  isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int):
            return self.km < other

    def __gt__(self, other: int):
        if  isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, int):
            return self.km > other

    def __le__(self, other: int):
        if  isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, int):
            return self.km <= other

    def __ge__(self, other: int):
        if  isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, int):
            return self.km >= other
