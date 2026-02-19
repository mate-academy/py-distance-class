from typing import Union


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, Distance):
            km_to_add = other.km
        else:
            km_to_add = other
        return Distance(self.km + km_to_add)

    def __iadd__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: Union[int, float]) -> "Distance":
        if not isinstance(other, (int, float)):
            raise TypeError("Can multiply Distance only by int or float")
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        if not isinstance(other, (int, float)):
            raise TypeError("Can divide Distance only by int or float")
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: Union[int, float, "Distance"]) -> bool:
        return self.km == (other.km if isinstance(other, Distance) else other)

    def __lt__(self, other: Union[int, float, "Distance"]) -> bool:
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: Union[int, float, "Distance"]) -> bool:
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: Union[int, float, "Distance"]) -> bool:
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: Union[int, float, "Distance"]) -> bool:
        return self.km >= (other.km if isinstance(other, Distance) else other)
