class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (float, int)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported operand type for +")

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            raise TypeError("Unsupported operand type for +=")

    def __mul__(self, other: "Distance") -> "Distance":
        if isinstance(other, (float, int)):
            return Distance(self.km * other)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other: "Distance") -> "Distance":
        if isinstance(other, (float, int)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("Unsupported operand type for /")

    def __lt__(self, other: "Distance") -> "Distance":
        return (self.km < other.km) if isinstance(other, Distance)\
            else (self.km < other)

    def __gt__(self, other: "Distance") -> "Distance":
        return (self.km > other.km) if isinstance(other, Distance)\
            else (self.km > other)

    def __eq__(self, other: "Distance") -> "Distance":
        return (self.km == other.km) if isinstance(other, Distance)\
            else (self.km == other)

    def __le__(self, other: "Distance") -> bool:
        return self.km <= other.km if isinstance(other, Distance)\
            else self.km <= other

    def __ge__(self, other: "Distance") -> bool:
        return self.km >= other.km if isinstance(other, Distance)\
            else self.km >= other
