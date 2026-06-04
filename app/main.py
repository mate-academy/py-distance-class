class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __radd__(self, other: int | float | "Distance") -> "Distance":
        return self.__add__(other)

    def __iadd__(self, other: int | float | "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float) -> "Distance":
        return Distance(self.km * other)

    def __rmul__(self, other: int | float) -> "Distance":
        return self.__mul__(other)

    def __truediv__(self, other: int | float) -> "Distance":
        calculated_distance = self.km / other
        return Distance(round(calculated_distance, 2))

    def _get_km(self, other: int | float | "Distance") -> int | float:
        if isinstance(other, Distance):
            return other.km
        return other

    def __lt__(self, other: int | float | "Distance") -> bool:
        return self.km < self._get_km(other)

    def __gt__(self, other: int | float | "Distance") -> bool:
        return self.km > self._get_km(other)

    def __eq__(self, other: int | float | "Distance") -> bool:
        return self.km == self._get_km(other)

    def __le__(self, other: int | float | "Distance") -> bool:
        return self.km <= self._get_km(other)

    def __ge__(self, other: int | float | "Distance") -> bool:
        return self.km >= self._get_km(other)
    