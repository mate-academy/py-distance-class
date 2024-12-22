class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: int) -> int:
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        elif isinstance(other, int):
            return Distance(
                km=self.km + other
            )

    def __iadd__(self, other: int) -> int:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, int):
            self.km += other
            return self

    def __mul__(self, other: int) -> int:
        if isinstance(other, Distance):
            self.km *= other.km
            return self
        elif isinstance(other, int):
            self.km *= other
            return self

    def __truediv__(self, other: int) -> float:
        if isinstance(other, Distance):
            self.km = round(self.km / other.km, 2)
            return self, 2
        elif isinstance(other, int):
            self.km = round(self.km / other, 2)
            return self

    def __lt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int):
            return self.km < other

    def __gt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, int):
            return self.km > other

    def __eq__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int):
            return self.km == other

    def __le__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km != other.km
        elif isinstance(other, int):
            return self.km != other

    def __ge__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, int):
            return self.km >= other
