from typing import Self, Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, distance: Union[Self, int, float]) -> Self:
        if isinstance(distance, (int, float)):
            return self.__class__(self.km + distance)
        return self.__class__(self.km + distance.km)

    def __iadd__(self, distance: Union[Self, int, float]) -> Self:
        self.km = self.__add__(distance).km
        return self

    def __mul__(self, num: Union[int, float]) -> Self:
        return self.__class__(self.km * num)

    def __truediv__(self, num: Union[int, float]) -> Self:
        return self.__class__(round(self.km / num, 2))

    def __eq__(self, distance: Union[Self, int, float]) -> bool:
        if isinstance(distance, (int, float)):
            return self.km == distance
        return self.km == distance.km

    def __gt__(self, distance: Union[Self, int, float]) -> bool:
        if isinstance(distance, (int, float)):
            return self.km > distance
        return self.km > distance.km

    def __lt__(self, distance: Union[Self, int, float]) -> bool:
        if isinstance(distance, (int, float)):
            return self.km < distance
        return self.km < distance.km

    def __ge__(self, distance: Union[Self, int, float]) -> bool:
        if isinstance(distance, (int, float)):
            return self.km >= distance
        return self.km >= distance.km

    def __le__(self, distance: Union[Self, int, float]) -> bool:
        if isinstance(distance, (int, float)):
            return self.km <= distance
        return self.km <= distance.km
