from typing import Union


class Distance:

    def __init__(self, km: float) -> None:
        """Ініціалізація об'єкта Distance."""
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        """Додає дві дистанції або дистанцію і число."""
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        elif isinstance(other, Distance):
            return Distance(self.km + other.km)
        return NotImplemented

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        """Додає до існуючого об'єкта дистанцію або число."""
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        else:
            return NotImplemented
        return self

    def __mul__(self, factor: Union[int, float]) -> "Distance":
        """Множить дистанцію на число."""
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)
        return NotImplemented

    def __truediv__(self, divisor: Union[int, float]) -> "Distance":
        """Ділить дистанцію на число (округлює до 2 знаків)."""
        if isinstance(divisor, (int, float)) and divisor != 0:
            return Distance(round(self.km / divisor, 2))
        return NotImplemented

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        return self.km == (other.km if isinstance(other, Distance) else other)

    def __ne__(self, other: Union["Distance", int, float]) -> bool:
        return self.km != (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        return self.km >= (other.km if isinstance(other, Distance) else other)
