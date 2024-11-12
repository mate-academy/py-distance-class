class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: None) -> None:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(km=self.km + other)
        else:
            raise TypeError(f"unsupported operand type(s) for +: "
                            f"Distance and {type(other)}")

    def __iadd__(self, other: None) -> None:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(f"unsupported operand type(s) for +: "
                            f"Distance and {type(other)}")
        return self

    def __mul__(self, koef: int) -> None:
        return Distance(km=self.km * koef)

    def __truediv__(self, num: int) -> None:
        if num == 0:
            return "Division by zero!"
        return Distance(round(self.km / num, 2))

    def __lt__(self, other: int) -> bool:
        return self.km < other

    def __gt__(self, other: int) -> bool:
        return self.km > other

    def __eq__(self, other: int) -> bool:
        return self.km == other

    def __le__(self, other: int) -> bool:
        return self.km <= other

    def __ge__(self, other: int) -> bool:
        return self.km >= other
