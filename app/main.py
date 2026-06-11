class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def _get_km(self, other: "Distance | int | float") -> float:
        return other.km if isinstance(other, Distance) else other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | int | float") -> "Distance":
        return Distance(self.km + self._get_km(other))

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        self.km += self._get_km(other)
        return self

    def __mul__(self, other: int | float) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: "Distance | int | float") -> bool:
        return self.km < self._get_km(other)

    def __gt__(self, other: "Distance | int | float") -> bool:
        return self.km > self._get_km(other)

    def __eq__(self, other: object) -> bool:
        return self.km == self._get_km(other)  # type: ignore[arg-type]

    def __le__(self, other: "Distance | int | float") -> bool:
        return self.km <= self._get_km(other)

    def __ge__(self, other: "Distance | int | float") -> bool:
        return self.km >= self._get_km(other)
