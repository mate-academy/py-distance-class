from ctypes import Union


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        if not isinstance(other, Distance):
            return None
        return Distance(self.km + other.km)

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        if not isinstance(other, Distance):
            return None
        self.km += other.km
        return self

    def __mul__(self, other: Union[int, float]) -> "Distance":
        if not isinstance(other, (int, float)):
            return None
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        if not isinstance(other, (int, float)):
            return None
        return round(Distance(self.km / other), 2)

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        if not isinstance(other, Distance):
            return None
        return self.km < other.km

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        if not isinstance(other, Distance):
            return None
        return self.km > other.km

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        if not isinstance(other, Distance):
            return None
        return self.km == other.km

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        if not isinstance(other, Distance):
            return None
        return self.km <= other.km

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        if not isinstance(other, Distance):
            return None
        return self.km >= other.km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return self.__repr__()
