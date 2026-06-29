class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_value(self, other: "Distance | int | float") -> float:
        return other.km if isinstance(other, Distance) else other

    def __add__(self, other: "Distance | int | float") -> "Distance":
        return Distance(self.km + self._get_value(other))

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        self.km += self._get_value(other)
        return self

    def __mul__(self, other: int | float) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: "Distance | int | float") -> bool:
        return self.km < self._get_value(other)

    def __gt__(self, other: "Distance | int | float") -> bool:
        return self.km > self._get_value(other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return False

    def __le__(self, other: "Distance | int | float") -> bool:
        return self.km <= self._get_value(other)

    def __ge__(self, other: "Distance | int | float") -> bool:
        return self.km >= self._get_value(other)
