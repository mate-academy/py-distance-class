from __future__ import annotations


class Distance:

    def __init__(self, km: float = 0.0) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def _convert_to_km(other: int | float | Distance) -> float:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, int | float):
            return float(other)
        raise TypeError("Unsupported type for arithmetic operation")

    def __add__(self, other: int | float | Distance) -> Distance:
        return Distance(self.km + self._convert_to_km(other))

    def __iadd__(self, other: int | float | Distance) -> Distance:
        self.km += self._convert_to_km(other)
        return self

    def __mul__(self, other: int | float | Distance) -> Distance:
        return Distance(self.km * self._convert_to_km(float(other)))

    def __truediv__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("Unsupported type for arithmetic operation")
        other_km = self._convert_to_km(other)
        return Distance(round(self.km / other_km, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        return self.km < self._convert_to_km(other)

    def __gt__(self, other: int | float | Distance) -> bool:
        return self.km > self._convert_to_km(other)

    def __eq__(self, other: int | float | Distance) -> bool:
        return self.km == self._convert_to_km(other)

    def __le__(self, other: int | float | Distance) -> bool:
        return not self.__gt__(other)

    def __ge__(self, other: int | float | Distance) -> bool:
        return not self.__lt__(other)
