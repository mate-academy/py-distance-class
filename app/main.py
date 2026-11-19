class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def _get_km(self, other: "int | float | Distance") -> int | float:
        return other.km if isinstance(other, Distance) else other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "int | float | Distance") -> "Distance":
        return Distance(self.km + self._get_km(other))

    def __iadd__(self, other: "int | float | Distance") -> "Distance":
        self.km += self._get_km(other)
        return self

    def __mul__(self, other: "int | float") -> "Distance":
        if isinstance(other, Distance):
            return NotImplemented
        return Distance(self.km * other)

    def __truediv__(self, other: "int | float") -> "Distance":
        if isinstance(other, Distance):
            return NotImplemented
        return Distance(round(self.km / self._get_km(other), 2))

    def __lt__(self, other: "int | float | Distance") -> bool:
        return self.km < self._get_km(other)

    def __gt__(self, other: "int | float | Distance") -> bool:
        return self.km > self._get_km(other)

    def __eq__(self, other: "int | float | Distance") -> bool:
        return self.km == self._get_km(other)

    def __le__(self, other: int | float | "Distance") -> bool:
        return self.km <= self._get_km(other)

    def __ge__(self, other: int | float | "Distance") -> bool:
        return self.km >= self._get_km(other)
