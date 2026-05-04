from typing import Self, Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, num: Union[int, float, Self]) -> "Distance":
        if isinstance(num, Distance):
            return Distance(self.km + num.km)
        if isinstance(num, (int, float)):
            return Distance(self.km + num)
        return NotImplemented

    def __iadd__(self, num: Union[int, float, Self]) -> Self:
        if isinstance(num, Distance):
            self.km += num.km
        if isinstance(num, (int, float)):
            self.km += num
        return self

    def __mul__(self, num: Union[int, float]) -> "Distance":
        if isinstance(num, (int, float)):
            return Distance(self.km * num)
        return NotImplemented

    def __truediv__(self, num: Union[int, float]) -> "Distance":
        if isinstance(num, (int, float)):
            return Distance(round(self.km / num, 2))
        return NotImplemented

    def __eq__(self, num: object) -> bool:
        if isinstance(num, Distance):
            return self.km == num.km
        if isinstance(num, (int, float)):
            return self.km == num
        return False

    def __lt__(self, num: Union[int, float, Self]) -> bool:
        if isinstance(num, Distance):
            return self.km < num.km
        if isinstance(num, (int, float)):
            return self.km < num
        return False

    def __le__(self, num: Union[int, float, Self]) -> bool:
        if isinstance(num, Distance):
            return self.km <= num.km
        if isinstance(num, (int, float)):
            return self.km <= num
        return False

    def __gt__(self, num: Union[int, float, Self]) -> bool:
        if isinstance(num, Distance):
            return self.km > num.km
        if isinstance(num, (int, float)):
            return self.km > num
        return False

    def __ge__(self, num: Union[int, float, Self]) -> bool:
        if isinstance(num, Distance):
            return self.km >= num.km
        if isinstance(num, (int, float)):
            return self.km >= num
        return False
