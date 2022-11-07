from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[object, int, float]) -> object:

        if isinstance(other, Union[float, int]):
            result = self.__class__(self.km + other)

        else:
            result = self.__class__(self.km + other.km)

        return result

    def __iadd__(self, other: Union[object, int, float]) -> object:

        if isinstance(other, Union[int, float]):
            setattr(self, "km", self.km + other)

        else:
            setattr(self, "km", self.km + other.km)

        return self

    def __mul__(self, other: Union[int, float]) -> object:
        return self.__class__(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> object:
        return self.__class__(round(self.km / other, 2))

    def __lt__(self, other: Union[object, int, float]) -> bool:
        if isinstance(other, Union[int, float]):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Union[object, int, float]) -> bool:
        if isinstance(other, Union[int, float]):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Union[object, int, float]) -> bool:
        if isinstance(other, Union[int, float]):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Union[object, int, float]) -> bool:
        if isinstance(other, Union[int, float]):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Union[object, int, float]) -> bool:
        if isinstance(other, Union[int, float]):
            return self.km >= other
        return self.km >= other.km

    def __len__(self) -> Union[float, int]:
        return self.km
