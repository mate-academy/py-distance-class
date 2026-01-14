from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float | int) -> Distance:
        return Distance(
            self.km + get_km(other))

    def __iadd__(self,
                 other: Distance | float | int
                 ) -> Distance | float | int:
        self.km = (self.km + get_km(other))
        return self

    def __mul__(self, other: float | int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float | int) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | float | int) -> bool:
        return self.km < get_km(other)

    def __gt__(self, other: Distance | float | int) -> bool:
        return self.km > get_km(other)

    def __eq__(self, other: Distance | float | int) -> bool:
        return self.km == get_km(other)

    def __le__(self, other: Distance | float | int) -> bool:
        return self.km <= get_km(other)

    def __ge__(self, other: Distance | float | int) -> bool:
        return self.km >= get_km(other)


def get_km(param: Distance | float | int) -> int | float:
    return param.km if isinstance(param, Distance) else param
