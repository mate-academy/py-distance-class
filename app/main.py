class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object | int | float) -> object:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __iadd__(self, other: object | int | float) -> object:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, number: int) -> int:
        self.km *= number
        return self

    def __truediv__(self, number: int) -> object:
        self.km = round(self.km / number, 2)
        return self

    def __lt__(self, other: object | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: object | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __le__(self, other: object | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: object | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other

    def __eq__(self, other: object | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other
