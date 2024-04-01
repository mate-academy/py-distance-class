class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            other = other.km
        return Distance(self.km + other)

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported operand type for +")
        return self

    def __mul__(self, scalar: float) -> "Distance":
        if isinstance(scalar, (int, float)):
            return Distance(self.km * scalar)
        raise TypeError("Unsupported operand type for *")

    def __truediv__(self, divisor: float) -> "Distance":
        if isinstance(divisor, (int, float)):
            result = self.km / divisor
            return Distance(round(result, 2))
        raise TypeError("Unsupported operand type for /")

    def __lt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        raise TypeError("Unsupported operand type for <")

    def __gt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        raise TypeError("Unsupported operand type for >")

    def __eq__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        raise TypeError("Unsupported operand type for ==")

    def __le__(self, other: "Distance") -> bool:
        return not self > other

    def __ge__(self, other: "Distance") -> bool:
        return not self < other
