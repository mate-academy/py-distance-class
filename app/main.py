class Distance:
    def __init__(self, km: int) -> None:
        if not isinstance(km, (int, float)):
            raise TypeError("Distance must be initialized with a number.")
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported operand type(s) for +")

    def __iadd__(self, other: float) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported operand type(s) for +=")
        return self

    def __mul__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("Unsupported operand type(s) for *")

    def __truediv__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("Unsupported operand type(s) for /")

    def __eq__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            return NotImplemented

    def __gt__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            return NotImplemented

    def __ge__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            return NotImplemented

    def __lt__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            return NotImplemented

    def __le__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            return NotImplemented
