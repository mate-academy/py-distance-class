class Distance:
    def __init__(self: "Distance", km: int) -> None:
        self.km = km

    def __str__(self: 'Distance') -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self: 'Distance') -> str:
        return f"Distance(km={self.km})"

    def __add__(self: "Distance", other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported operand type for +")

    def __iadd__(self: "Distance", other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported operand type for +=")
        return self

    def __mul__(self: "Distance", other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self: "Distance", other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("Unsupported operand type for /")

    def __lt__(self: "Distance", other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError("Unsupported operand type for <")

    def __gt__(self: "Distance", other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError("Unsupported operand type for >")

    def __eq__(self: "Distance", other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError("Unsupported operand type for ==")

    def __le__(self: "Distance", other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError("Unsupported operand type for <=")

    def __ge__(self: "Distance", other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError("Unsupported operand type for >=")
