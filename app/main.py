class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str :
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> Distance:
        return Distance(self.km + other)

    def __iadd__(self, other: int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __radd__(self, other: int) -> Distance:
        return Distance(self.km + other)

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if other == 0:
            raise ZeroDivisionError("division by zero")
        result = self.km / other
        result = round(result, 2)
        return Distance(result)

    def __lt__(self, other : Distance) -> Distance:
        return self.km < other

    def __gt__(self, other : bool) -> Distance:
        return self.km > other

    def __eq__(self, other : bool) -> Distance:
        return self.km == other

    def __le__(self, other : bool) -> Distance:
        return self.km <= other

    def __ge__(self, other : bool) -> Distance:
        return self.km >= other
