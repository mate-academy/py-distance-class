class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, sec: int) -> None:
        if type(sec) == int or type(sec) == float:
            self.km += sec
            return self
        else:
            self.km += sec.km
            return self

    def __iadd__(self, sec: int) -> int:
        if type(sec) == int or type(sec) == float:
            self.km += sec
            return self
        else:
            self.km += sec.km
            return self

    def __mul__(self, other: int) -> int:
        if type(other) == int:
            self.km *= other
            return self
        else:
            self.km *= other
            return self

    def __truediv__(self, other: int) -> float:
        if type(other) == int or type(other) == float:
            self.km = round(self.km / other, 2)
            return self

    def __lt__(self, other: int) -> bool:
        if type(other) == float or type(other) == int:
            return self.km < other
        else:
            return self.km < other.km

    def __gt__(self, other: float) -> bool:
        if type(other) == float or type(other) == int:
            return self.km > other
        else:
            return self.km > other.km

    def __eq__(self, other: float) -> bool:
        if type(other) == float or type(other) == int:
            return self.km == other
        else:
            return self.km == other.km

    def __le__(self, other: float) -> bool:
        if type(other) == float or type(other) == int:
            return self.km <= other
        else:
            return self.km <= other.km

    def __ge__(self, other: float) -> bool:
        if type(other) == float or type(other) == int:
            return self.km >= other
        else:
            return self.km >= other.km
