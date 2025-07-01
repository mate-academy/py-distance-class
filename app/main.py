class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, second: object | int) -> object:
        if isinstance(second, Distance):
            return Distance(self.km + second.km)
        return Distance(self.km + second)

    def __iadd__(self, other: object) -> object:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, mult: int) -> object:
        if isinstance(mult, int):
            return Distance(self.km * mult)
        raise TypeError

    def __truediv__(self, divide: int) -> object:
        if isinstance(divide, (int, float)):
            return Distance(round(self.km / divide, 2))
        raise TypeError

    def __lt__(self, other: object | int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: object | int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: object | int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: object | int) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: object | int) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
