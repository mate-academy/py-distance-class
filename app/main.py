class Distance:
    # Write your code here
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float) -> int | float:
        if isinstance(other, Distance):
            self.km = self.km + other.km
            return self

        elif isinstance(other, int | float):
            self.km = self.km + other
            return self

    def __iadd__(self, other: int | float) -> int | float:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, int | float):
            self.km += other
            return self

    def __mul__(self, other: int | float) -> int | float:
        self.km = self.km * other
        return self

    def __truediv__(self, other: int | float) -> int | float:
        self.km = round(self.km / other, 2)
        return self

    def __lt__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int | float):
            return self.km < other

    def __gt__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, int | float):
            return self.km > other

    def __eq__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int | float):
            return self.km == other

    def __le__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, int | float):
            return self.km <= other

    def __ge__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, int | float):
            return self.km >= other
