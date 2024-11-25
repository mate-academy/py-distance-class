class Distance:
    def __init__(self, km: float) -> None:
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
        raise TypeError(
            f"Unsupported operand type(s) for +: 'Distance' and '{type(other).__name__}'"
        )

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +=: 'Distance' and '{type(other).__name__}'"
            )
        return self

    def __mul__(self, factor: float) -> "Distance":
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)
        raise TypeError(
            f"Unsupported operand type(s) for *: 'Distance' and '{type(factor).__name__}'"
        )

    def __truediv__(self, divisor: float) -> "Distance":
        if isinstance(divisor, (int, float)):
            return Distance(round(self.km / divisor, 2))
        raise TypeError(
            f"Unsupported operand type(s) for /: 'Distance' and '{type(divisor).__name__}'"
        )

    def __lt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km < (other.km if isinstance(other, Distance) else other)
        return NotImplemented

    def __gt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km > (other.km if isinstance(other, Distance) else other)
        return NotImplemented

    def __eq__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km == (other.km if isinstance(other, Distance) else other)
        return NotImplemented

    def __le__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km <= (other.km if isinstance(other, Distance) else other)
        return NotImplemented

    def __ge__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km >= (other.km if isinstance(other, Distance) else other)
        return NotImplemented
