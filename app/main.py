class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> "Distance":
        if isinstance(other, Distance):
            self.km = self.km + other.km
            return Distance(
                self.km
            )
        else:
            self.km = self.km + other.real
            return Distance(
                self.km
            )

    def __iadd__(self, other: int) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("Unsupported operand type(s)")

    def __truediv__(self, other: int) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("Unsupported operand type(s)")

    def __lt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km

        else:
            return self.km < other.real

    def __gt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km

        else:
            return self.km > other.real

    def __le__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km

        else:
            return self.km <= other.real

    def __ge__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km

        else:
            return self.km >= other.real

    def __eq__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km

        else:
            return self.km == other.real
