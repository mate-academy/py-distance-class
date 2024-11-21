from typing import TypeVar, Union

Self = TypeVar("Self", bound="Distance")


class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self: Self, distance: Union["Distance", int, float]) -> Self:
        if isinstance(distance, (int, float)):
            return self.__class__(self.km + distance)
        return self.__class__(self.km + distance.km)

    def __iadd__(self: Self, distance: Union[Self, int, float]) -> Self:
        self.km = (self + distance).km
        return self

    def __mul__(self: Self, num: Union[int, float]) -> Self:
        return self.__class__(self.km * num)

    def __truediv__(self: Self, num: Union[int, float]) -> Self:
        return self.__class__(round(self.km / num, 2))

    def __eq__(self, distance: Union[Self, int, float]) -> bool:
        return self.km == distance

    def __gt__(self, distance: Union[Self, int, float]) -> bool:
        return self.km > distance

    def __lt__(self, distance: Union[Self, int, float]) -> bool:
        return self.km < distance

    def __ge__(self, distance: Union[Self, int, float]) -> bool:
        return self.km >= distance

    def __le__(self, distance: Union[Self, int, float]) -> bool:
        return self.km <= distance
