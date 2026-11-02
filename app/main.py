class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) \
            -> Distance | NotImplemented:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        elif isinstance(other, (int, float)):
            self.km = self.km + other
        else:
            return NotImplemented
        return self

    def __iadd__(self, other: Distance | int | float) \
            -> Distance | NotImplemented:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented

        return self

    def __mul__(self, other: Distance | int | float) \
            -> Distance | NotImplemented:
        if isinstance(other, (int, float)):
            return Distance(round(self.km * other, 3))
        else:
            return NotImplemented

    def __truediv__(self, other: int | float) -> Distance | NotImplemented:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            return NotImplemented

    def __lt__(self, other: int | float) -> bool:
        return self.km < other

    def __gt__(self, other: int | float) -> bool:
        return self.km > other

    def __eq__(self, value: object, /) -> bool:
        return self.km == value

    def __le__(self, other: int | float) -> bool:
        return self.km <= other

    def __ge__(self, other: int | float) -> bool:
        return self.km >= other
