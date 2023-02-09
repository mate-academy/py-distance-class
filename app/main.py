from typing import Union, Any


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    @staticmethod
    def verify_data(other: Union[int, float]) -> Union[int, float]:
        if isinstance(other, Distance):
            return other.km
        return other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, Any]) -> Any:
        value = self.verify_data(other)
        return Distance(self.km + value)

    def __iadd__(self, other: Union[int, float, Any]) -> Any:
        value = self.verify_data(other)
        self.km = self + value
        return self

    def __mul__(self, other: Union[int, float]) -> Any:
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> Any:
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: Union[int, float]) -> bool:
        value = self.verify_data(other)
        return self.km == value

    def __lt__(self, other: Union[int, float]) -> bool:
        value = self.verify_data(other)
        return self.km < value

    def __gt__(self, other: Union[int, float]) -> bool:
        value = self.verify_data(other)
        return self.km > value

    def __le__(self, other: Union[int, float]) -> bool:
        value = self.verify_data(other)
        return self.km <= value

    def __ge__(self, other: Union[int, float]) -> bool:
        value = self.verify_data(other)
        return self.km >= value
