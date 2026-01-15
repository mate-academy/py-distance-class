class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _other_km(self, other: object) -> float:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return float(other)
        raise TypeError("Unsupported type for operation with Distance")

    def __add__(self, other: object) -> "Distance":
        try:
            other_km = self._other_km(other)
        except TypeError:
            return NotImplemented  # type: ignore[return-value]
        return Distance(self.km + other_km)

    def __radd__(self, other: object) -> "Distance":
        return self.__add__(other)

    def __iadd__(self, other: object) -> "Distance":
        try:
            other_km = self._other_km(other)
        except TypeError:
            return NotImplemented  # type: ignore[return-value]
        self.km += other_km
        return self

    def __mul__(self, other: int | float) -> "Distance":
        if not isinstance(other, (int, float)):
            return NotImplemented  # type: ignore[return-value]
        return Distance(self.km * float(other))

    def __rmul__(self, other: int | float) -> "Distance":
        return self.__mul__(other)

    def __truediv__(self, other: int | float) -> "Distance":
        if not isinstance(other, (int, float)):
            return NotImplemented  # type: ignore[return-value]
        if other == 0:
            raise ZeroDivisionError("division by zero")
        return Distance(round(self.km / float(other), 2))

    def __lt__(self, other: object) -> bool:
        try:
            other_km = self._other_km(other)
        except TypeError:
            return NotImplemented  # type: ignore[return-value]
        return self.km < other_km

    def __gt__(self, other: object) -> bool:
        try:
            other_km = self._other_km(other)
        except TypeError:
            return NotImplemented  # type: ignore[return-value]
        return self.km > other_km

    def __eq__(self, other: object) -> bool:
        try:
            other_km = self._other_km(other)
        except TypeError:
            return NotImplemented  # type: ignore[return-value]
        return self.km == other_km

    def __le__(self, other: object) -> bool:
        try:
            other_km = self._other_km(other)
        except TypeError:
            return NotImplemented  # type: ignore[return-value]
        return self.km <= other_km

    def __ge__(self, other: object) -> bool:
        try:
            other_km = self._other_km(other)
        except TypeError:
            return NotImplemented  # type: ignore[return-value]
        return self.km >= other_km
