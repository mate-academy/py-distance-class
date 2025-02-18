from typing import Union


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Union[int, float, "Distance"]) -> "Distance":
        value_to_compare = other.km if isinstance(other, Distance) else other
        return Distance(self.km + value_to_compare)

    def __iadd__(self, other: Union[int, float, "Distance"]) -> "Distance":
        value_to_compare = other.km if isinstance(other, Distance) else other
        self.km = self.km + value_to_compare
        return self

    def __mul__(self, other: int) -> "Distance":
        return Distance(
            self.km * other
        )

    def __truediv__(self, other: int) -> "Distance":
        return Distance(
            round(self.km / other, 2)
        )

    def __lt__(self, other: Union[int, float, "Distance"]) -> bool:
        value_to_compare = other.km if isinstance(other, Distance) else other
        return self.km < value_to_compare

    def __le__(self, other: Union[int, float, "Distance"]) -> bool:
        value_to_compare = other.km if isinstance(other, Distance) else other
        return self.km <= value_to_compare

    def __gt__(self, other: Union[int, float, "Distance"]) -> bool:
        value_to_compare = other.km if isinstance(other, Distance) else other
        return self.km > value_to_compare

    def __ge__(self, other: Union[int, float, "Distance"]) -> bool:
        value_to_compare = other.km if isinstance(other, Distance) else other
        return self.km >= value_to_compare

    def __eq__(self, other: Union[int, float, "Distance"]) -> bool:
        value_to_compare = other.km if isinstance(other, Distance) else other
        return self.km == value_to_compare

    def __ne__(self, other: Union[int, float, "Distance"]) -> bool:
        value_to_compare = other.km if isinstance(other, Distance) else other
        return self.km != value_to_compare
