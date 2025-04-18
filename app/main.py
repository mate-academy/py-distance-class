class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"
    
    def __add__(self, other: int) -> int:
        return self.km + self.other

    def __iadd__(self, other: int) -> int:
        self.km += self.other
        return self.km

    def __mul__(self, other: int) -> int:
        return self.km * self.other

    def __truediv__(self, other: int) -> int:
        return self.km / self.other

    def __lt__(self, other: int) -> bool:
        return self.km < self.other

    def __eq__(self, other: int) -> bool:
        if isinstance(other, Distance):
            if self.km == self.other:
                return True
        return False

    def __gt__(self, other: int) -> bool:
        return self.km > self.other

    def __le__(self, other: int) -> bool:
        return self.km <= self.other

    def __ge__(self, other: int) -> bool:
        return self.km >= self.other
