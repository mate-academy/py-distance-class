class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> None:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __iadd__(self, other: object) -> None:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: object) -> None:
        self.km *= other
        return self

    def __truediv__(self, other: object) -> None:
        if isinstance(other, (int, float)) and other != 0:
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: object) -> None:
        if self.km < other:
            return True
        else:
            return False

    def __gt__(self, other: object) -> None:
        if self.km > other:
            return True
        else:
            return False

    def __eq__(self, other: object) -> None:
        if self.km == other:
            return True
        else:
            return False

    def __le__(self, other: object) -> None:
        if self.km <= other:
            return True
        else:
            return False

    def __ge__(self, other: object) -> None:
        if self.km >= other:
            return True
        else:
            return False
