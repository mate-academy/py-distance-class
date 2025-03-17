class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, factor: "int | float") -> "Distance":
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)
        return NotImplemented

    def __truediv__(self, divisor: "int | float") -> "Distance":
        if isinstance(divisor, (int, float)) and divisor != 0:
            return Distance(round(self.km / divisor, 2))
        return NotImplemented

    def __lt__(self, other: "Distance | int | float") -> bool:
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: "Distance | int | float") -> bool:
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __eq__(self, other: "Distance | int | float") -> bool:
        return self.km == (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: "Distance | int | float") -> bool:
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: "Distance | int | float") -> bool:
        return self.km >= (other.km if isinstance(other, Distance) else other)
