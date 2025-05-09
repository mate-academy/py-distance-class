from typing import Union


class Distance:
    def __init__(self, km: int) -> None:
        if not isinstance(km, int):
            raise TypeError("km must be integer")
        else:
            self.km = km

    def __str__(self) -> str:
        # distance = Distance(self.km)
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        elif isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            raise TypeError("Unsupported type")

    def __iadd__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        else:
            raise TypeError("Unsupported type")
        return self

    def __mul__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        elif isinstance(other, Distance):
            raise TypeError("Multiplication by Distance not supported")
        else:
            raise TypeError("Unsupported type")

    def __truediv__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        elif isinstance(other, Distance):
            raise TypeError("Multiplication by Distance not supported")
        else:
            raise TypeError("Unsupported type")

    def __lt__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError("Unsupported type")

    def __gt__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError("Unsupported type")

    def __eq__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError("Unsupported type")

    def __le__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError("Unsupported type")

    def __ge__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError("Unsupported type")
