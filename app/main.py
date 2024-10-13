from __future__ import annotations
from typing import Union


class Distance:

    def __init__(self, km: float) -> None:
        if not isinstance(km, (int, float)) or km <= 0:
            raise ValueError(
                "Distance in kilometers must be a positive number."
            )

        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _convert_to_distance(
            self, other: Union[Distance, float, int]
    ) -> Distance:

        if isinstance(other, Distance):
            return other
        elif isinstance(other, (int, float)):
            return Distance(float(other))
        else:
            raise TypeError(
                f"Unsupported type(s): 'Distance' and '{type(other).__name__}'"
            )

    def __add__(self, other: Union[Distance, float, int]) -> Distance:
        other = self._convert_to_distance(other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Union[Distance, float, int]) -> Distance:
        other = self._convert_to_distance(other)
        self.km += other.km
        return self

    def __mul__(self, other: Union[float, int]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * float(other))
        else:
            raise TypeError(
                f"Unsupported operand type(s) for *: 'Distance' and "
                f"'{type(other).__name__}'"
            )

    def __truediv__(self, other: Union[float, int]) -> Distance:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide Distance by zero.")
            result = self.km / other
            return Distance(round(result, 2))
        else:
            raise TypeError(
                f"Unsupported operand type(s) for "
                f"/: 'Distance' and '{type(other).__name__}'"
            )

    def __lt__(self, other: Union[Distance, float, int]) -> bool:
        other = self._convert_to_distance(other)
        return self.km < other.km

    def __gt__(self, other: Union[Distance, float, int]) -> bool:
        other = self._convert_to_distance(other)
        return self.km > other.km

    def __eq__(self, other: Union[Distance, float, int]) -> bool:
        other = self._convert_to_distance(other)
        return self.km == other.km

    def __le__(self, other: Union[Distance, float, int]) -> bool:
        other = self._convert_to_distance(other)
        return self.km <= other.km

    def __ge__(self, other: Union[Distance, float, int]) -> bool:
        other = self._convert_to_distance(other)
        return self.km >= other.km
