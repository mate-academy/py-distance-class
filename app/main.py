class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __eq__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return False

    def __lt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __le__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError(f"Unsupported operand type for +: "
                        f"'Distance' and {type(other)}")

    def __sub__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km - other.km)
        return NotImplemented

    def __ge__(self, other: "Distance") -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented

    def __gt__(self, other: "Distance") -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __mul__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError(f"Unsupported operand "
                        f"type for *: 'Distance' and {type(other)}")

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self

    def __truediv__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            raise TypeError("Unsupported operand type for /: "
                            "'Distance' and 'Distance'")
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Division by zero is not allowed")
            return Distance(round(self.km / other, 2))
        raise TypeError(f"Unsupported operand type for /: "
                        f"'Distance' and {type(other)}")
