class Distance:
    def __init__(self, km: int | float) -> None:
        self.km: int | float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def _to_number(self, other: "Distance | int | float") -> int | float:
        return other.km if isinstance(other, Distance) else other

    def __lt__(self, other: "Distance | int | float") -> bool:
        return self.km < self._to_number(other)

    def __gt__(self, other: "Distance | int | float") -> bool:
        return self.km > self._to_number(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return False
        return self.km == self._to_number(other)

    def __le__(self, other: "Distance | int | float") -> bool:
        return self.km <= self._to_number(other)

    def __ge__(self, other: "Distance | int | float") -> bool:
        return self.km >= self._to_number(other)
