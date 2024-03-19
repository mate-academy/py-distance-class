class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported operand for:+ operation")

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported operand for for:+= operation")
        return self

    def __mul__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("Unsupported operand for:* operation")

    def __truediv__(self, other: (int, float)) -> "Distance":
        if isinstance(other, (int, float)):
            result = self.km / other
            return Distance(round(result, 2))
        else:
            raise TypeError("Unsupported operand for:/ operation")

    def __lt__(self, other: ("Distance", float, int)) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (float, int)):
            return self.km < other
        else:
            raise TypeError("Unsupported operand for bool operation")

    def __gt__(self, other: ("Distance", float, int)) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (float, int)):
            return self.km > other
        else:
            raise TypeError("Unsupported operand for bool operation")

    def __eq__(self, other: ("Distance", float, int)) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (float, int)):
            return self.km == other
        else:
            raise TypeError("Unsupported operand for bool operation")

    def __le__(self, other: ("Distance", float, int)) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (float, int)):
            return self.km <= other
        else:
            raise TypeError("Unsupported operand for bool operation")

    def __ge__(self, other: ("Distance", float, int)) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (float, int)):
            return self.km >= other
        else:
            raise TypeError("Unsupported operand for bool operation")
