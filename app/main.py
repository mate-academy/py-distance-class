class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_km(self, other: "Distance" | int | float) -> float:
        return other.km if isinstance(other, Distance) else other

    def __add__(self, other: "Distance" | int | float) -> "Distance":
        result = self.km + self._get_km(other)
        return Distance(result)

    def __iadd__(self, other: "Distance" | int | float) -> "Distance":
        self.km += self._get_km(other)
        return self

    def __mul__(self, multiplier: int | float) -> "Distance":
        result = self.km * multiplier
        return Distance(result)

    def __truediv__(self, divider: int | float) -> "Distance":
        result = round(self.km / divider, 2)
        return Distance(result)

    def __lt__(self, other: "Distance" | int | float) -> bool:
        return self.km < self._get_km(other)

    def __gt__(self, other: "Distance" | int | float) -> bool:
        return self.km > self._get_km(other)

    def __eq__(self, other: "Distance" | int | float) -> bool:
        return self.km == self._get_km(other)

    def __le__(self, other: "Distance" | int | float) -> bool:
        return self.km <= self._get_km(other)

    def __ge__(self, other: "Distance" | int | float) -> bool:
        return self.km >= self._get_km(other)
