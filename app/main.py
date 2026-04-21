class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_km(self, other: "Distance | float") -> float:
        return other.km if isinstance(other, Distance) else other

    def __add__(self, other: "Distance | float") -> "Distance":
        return Distance(self.km + self._get_km(other))

    def __iadd__(self, other: "Distance | float") -> "Distance":
        self.km += self._get_km(other)
        return self

    def __mul__(self, factor: float) -> "Distance":
        return Distance(self.km * factor)

    def __truediv__(self, divisor: float) -> "Distance":
        return Distance(round(self.km / divisor, 2))

    def __lt__(self, other: "Distance | float") -> bool:
        return self.km < self._get_km(other)

    def __gt__(self, other: "Distance | float") -> bool:
        return self.km > self._get_km(other)

    def __eq__(self, other: "Distance | float") -> bool:
        return self.km == self._get_km(other)

    def __le__(self, other: "Distance | float") -> bool:
        return self.km <= self._get_km(other)

    def __ge__(self, other: "Distance | float") -> bool:
        return self.km >= self._get_km(other)
