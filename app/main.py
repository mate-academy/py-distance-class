class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __add__(self, other: object | int | float) -> object:
        if isinstance(other, int | float):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __iadd__(self, other: object | int | float) -> object:
        if isinstance(other, int | float):
            self.km += other
            return self
        self.km += other.km
        return self

    def __mul__(self, other: int | float) -> object | None:
        if isinstance(other, int | float):
            return Distance(self.km * other)
        return None

    def __truediv__(self, other: int | float) -> object | None:
        if isinstance(other, int | float):
            return Distance(round(self.km / other, 2))
        return None

    def __lt__(self, other: object | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: object | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: object | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: object | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: object | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km >= other
        return self.km >= other.km
