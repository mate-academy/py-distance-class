class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, second: object | int) -> object:
        return Distance(self.km + getattr(second, "km", second))

    def __iadd__(self, other: object | int) -> object:
        self.km += getattr(other, "km", other)
        return self

    def __mul__(self, mul: int) -> object:
        self.km *= mul
        return self

    def __truediv__(self, devv: int) -> object:
        if devv == 0:
            return float("inf")
        self.km = round(self.km / devv, 2)
        return self

    def __lt__(self, sec: object | int) -> bool:
        return self.km < getattr(sec, "km", sec)

    def __gt__(self, sec: object | int) -> bool:
        return self.km > getattr(sec, "km", sec)

    def __eq__(self, sec: object | int) -> bool:
        return self.km == getattr(sec, "km", sec)

    def __le__(self, sec: object | int) -> bool:
        return self.km <= getattr(sec, "km", sec)

    def __ge__(self, sec: object | int) -> bool:
        return self.km >= getattr(sec, "km", sec)
