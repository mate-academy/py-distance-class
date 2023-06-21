from __future__ import annotations
from typing import Any


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def _distance_types_validator(
            obj: Any,
            valid_types: tuple,
            operator: str
    ) -> None:
        if not isinstance(obj, valid_types):
            raise TypeError(
                f"TypeError: unsupported operand type(s) for {operator}: "
                f"'Distance' and '{type(obj)}'"
            )

    def __add__(self, other: Distance | int | float) -> Distance:

        self._distance_types_validator(
            obj=other,
            valid_types=(Distance, int, float),
            operator="+"
        )

        if isinstance(other, Distance):
            other = other.km

        return Distance(km=self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:

        self._distance_types_validator(
            obj=other,
            valid_types=(Distance, int, float),
            operator="+="
        )

        self.km = self + other

        return self

    def __mul__(self, other: int | float) -> Distance:

        self._distance_types_validator(
            obj=other,
            valid_types=(int, float),
            operator="*"
        )

        return Distance(km=self.km * other)

    def __truediv__(self, other: int | float) -> Distance:

        self._distance_types_validator(
            obj=other,
            valid_types=(int, float),
            operator="/"
        )

        km = self.km / other
        round_km = int(km) if int(km) == km else float("{:.2f}".format(km))
        return Distance(km=round_km)

    def __lt__(self, other: Distance | int | float) -> bool:

        self._distance_types_validator(
            obj=other,
            valid_types=(Distance, int, float),
            operator="<"
        )

        if isinstance(other, Distance):
            other = other.km

        return self.km < other

    def __gt__(self, other: Distance | int | float) -> bool:
        self._distance_types_validator(
            obj=other,
            valid_types=(Distance, int, float),
            operator=">"
        )

        if isinstance(other, Distance):
            other = other.km

        return self.km > other

    def __eq__(self, other: Distance | int | float) -> bool:
        self._distance_types_validator(
            obj=other,
            valid_types=(Distance, int, float),
            operator="=="
        )

        if isinstance(other, Distance):
            other = other.km

        return self.km == other

    def __le__(self, other: Distance | int | float) -> bool:
        self._distance_types_validator(
            obj=other,
            valid_types=(Distance, int, float),
            operator="<="
        )

        if isinstance(other, Distance):
            other = other.km

        return self.km <= other

    def __ge__(self, other: Distance | int | float) -> bool:
        self._distance_types_validator(
            obj=other,
            valid_types=(Distance, int, float),
            operator=">="
        )

        if isinstance(other, Distance):
            other = other.km

        return self.km >= other
