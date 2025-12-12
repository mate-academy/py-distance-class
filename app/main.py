from __future__ import annotations
from typing import Union

# Helper type for clean type hinting
DistanceOrNumber = Union[float, int, 'Distance']


class Distance:
    def __init__(self: Distance, km: float) -> None:
        self.km = km

    def _get_km_value(self, other: DistanceOrNumber) -> float | int:
        """Helper to extract the km value from Distance object or return the number."""
        if isinstance(other, Distance):
            return other.km
        return other

    def __str__(self: Distance) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self: Distance) -> str:
        return f"Distance(km={self.km})"

    def __add__(self: Distance, other: DistanceOrNumber) -> Distance:
        value = self._get_km_value(other)
        return Distance(self.km + value)

    def __iadd__(self: Distance, other: DistanceOrNumber) -> Distance:
        value = self._get_km_value(other)
        self.km += value
        return self

    def __mul__(self: Distance, other: float | int) -> Distance:
        # other тут майже завжди буде числом, якщо ми не реалізуємо __rmul__
        # і користувач напише 5 * Distance.
        result = self.km * other
        return Distance(result)

    def __truediv__(self: Distance, other: DistanceOrNumber) -> Distance:
        """
        Виправлено: тепер підтримується ділення на Distance або число.
        """
        value = self._get_km_value(other)

        if value == 0:
            raise ZeroDivisionError("Cannot divide Distance by zero.")

        result = round(self.km / value, 2)
        return Distance(result)

    def __lt__(self: Distance, other: DistanceOrNumber) -> bool:
        value = self._get_km_value(other)
        return self.km < value

    def __gt__(self: Distance, other: DistanceOrNumber) -> bool:
        value = self._get_km_value(other)
        return self.km > value

    def __eq__(self: Distance, other: DistanceOrNumber) -> bool:
        value = self._get_km_value(other)
        return self.km == value

    def __le__(self: Distance, other: DistanceOrNumber) -> bool:
        value = self._get_km_value(other)
        return self.km <= value

    def __ge__(self: Distance, other: DistanceOrNumber) -> bool:
        value = self._get_km_value(other)
        return self.km >= value