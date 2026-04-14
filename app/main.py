class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return (f"Distance: {self.km} kilometers.")

    def __repr__(self) -> str:
        return (f"Distance(km={self.km})")

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, int) or isinstance(other, float):
            distance = Distance(self.km + other)
        elif isinstance(other, Distance):
            distance = Distance(self.km + other.km)
        return distance

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, int) or isinstance(other, float):
            self.km += other
        elif isinstance(other, Distance):
            self.km = self.km + other.km
        return self

    def __mul__(self, other: int | float) -> Distance:
        distance = Distance(self.km * other)
        return distance

    def __truediv__(self, other: int | float) -> Distance:
        if other != 0:
            km = round(self.km / other, 2)
            distance = Distance(km)
            return distance
        else:
            print("Division par zéro")

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance) :
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, value: Distance | int | float) -> bool:
        return self.km == value

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
