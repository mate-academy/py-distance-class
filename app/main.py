from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def get_value(self, other: int) -> Any:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        else:
            return NotImplemented

    def __add__(self, other: int) -> "Distance":
        value = self.get_value(other)
        if value is not NotImplemented:
            return Distance(self.km + value)
        else:
            return NotImplemented

    def __iadd__(self, other: int) -> "Distance":
        value = self.get_value(other)
        if value is not NotImplemented:
            self.km += value
            return self
        else:
            return NotImplemented

    def __mul__(self, other: int) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            return NotImplemented

    def __truediv__(self, other: int) -> "Distance":
        if isinstance(other, (int, float)) and other != 0:
            return Distance(round(self.km / other, 2))
        else:
            return NotImplemented

    def __lt__(self, other: int) -> bool:
        value = self.get_value(other)
        if value is not NotImplemented:
            return self.km < value
        else:
            return NotImplemented

    def __gt__(self, other: int) -> bool:
        value = self.get_value(other)
        if value is not NotImplemented:
            return self.km > value
        else:
            return NotImplemented

    def __le__(self, other: int) -> bool:
        value = self.get_value(other)
        if value is not NotImplemented:
            return self.km <= value
        else:
            return NotImplemented

    def __ge__(self, other: int) -> bool:
        value = self.get_value(other)
        if value is not NotImplemented:
            return self.km >= value
        else:
            return NotImplemented

    def __eq__(self, other: int) -> bool:
        value = self.get_value(other)
        if value is not NotImplemented:
            return self.km == value
        else:
            return NotImplemented
