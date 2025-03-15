from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def _to_distance(other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(other)
        return other

    def __add__(self, other: Union[int, float, "Distance"]) -> "Distance":
        other = self._to_distance(other)
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return NotImplemented

    def __iadd__(self, other: Union[int, float, "Distance"]) -> "Distance":
        other = self._to_distance(other)
        if isinstance(other, Distance):
            self.km += other.km
            return self
        return NotImplemented

    def __mul__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, (int, float)) and float != 0:
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __lt__(self, other: Union[int, float, "Distance"]) -> bool:
        other = self._to_distance(other)
        if isinstance(other, Distance):
            return self.km < other.km
        return False

    def __gt__(self, other: Union[int, float, "Distance"]) -> bool:
        other = self._to_distance(other)
        distance1 = self.km
        distance2 = other.km
        if isinstance(other, Distance):
            return distance1 > distance2
        return False

    def __eq__(self, other: Union[int, float, "Distance"]) -> bool:
        other = self._to_distance(other)
        distance1 = self.km
        distance2 = other.km
        if isinstance(other, Distance):
            return distance1 == distance2
        return False

    def __le__(self, other: Union[int, float, "Distance"]) -> bool:
        other = self._to_distance(other)
        distance1 = self.km
        distance2 = other.km
        if isinstance(other, Distance):
            return distance1 <= distance2
        return False

    def __ge__(self, other: Union[int, float, "Distance"]) -> bool:
        other = self._to_distance(other)
        distance1 = self.km
        distance2 = other.km
        if isinstance(other, Distance):
            return distance1 >= distance2
        return False
