class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_km(self, other: "Distance | int | float") -> float:
        if isinstance(other, Distance):
            return other.km
        return other

    def __add__(self, other: "Distance | int | float") -> "Distance":
        new_km = self._get_km(other)
        new_distance = Distance(self.km + new_km)
        return new_distance

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        num = self._get_km(other)
        self.km += num
        return self

    def __mul__(self, other: int | float) -> "Distance":
        new_mul = Distance(self.km * other)
        return new_mul

    def __truediv__(self, other: int | float) -> "Distance":
        new_divide = Distance(round(self.km / other, 2))
        return new_divide

    def __lt__(self, other: "Distance | int | float") -> bool:
        return self.km < self._get_km(other)

    def __gt__(self, other: "Distance | int | float") -> bool:
        return self.km > self._get_km(other)

    def __eq__(self, other: "Distance | int | float") -> bool:
        return self.km == self._get_km(other)

    def __le__(self, other: "Distance | int | float") -> bool:
        return self.km <= self._get_km(other)

    def __ge__(self, other: "Distance | int | float") -> bool:
        return self.km >= self._get_km(other)
