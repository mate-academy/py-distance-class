class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_value(self, other: "Distance | float | int") -> float | int:
        return other.km if isinstance(other, Distance) else other

    def __add__(self, other: "Distance | float | int") -> "Distance":
        return Distance(self.km + self._get_value(other))

    def __radd__(self, other: float | int) -> "Distance":
        return self.__add__(other)

    def __iadd__(self, other: "Distance | float | int") -> "Distance":
        self.km += self._get_value(other)
        return self

    def __mul__(self, other: float | int) -> "Distance":
        if isinstance(other, Distance):
            return None
        return Distance(self.km * other)

    def __rmul__(self, other: float | int) -> "Distance":
        return self.__mul__(other)

    def __truediv__(self, other: float | int) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: "Distance | float | int") -> bool:
        return self.km < self._get_value(other)

    def __gt__(self, other: "Distance | float | int") -> bool:
        return self.km > self._get_value(other)

    def __eq__(self, other: "Distance | float | int") -> bool:
        return self.km == self._get_value(other)

    def __le__(self, other: "Distance | float | int") -> bool:
        return self.km <= self._get_value(other)

    def __ge__(self, other: "Distance | float | int") -> bool:
        return self.km >= self._get_value(other)
