from typing import Union


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError(f"Unsupported type {type(other)} for addition")

    def __iadd__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(f"Unsupported type {type(other)} for addition")
        return self

    def __mul__(self, other: int | float) -> "Distance":
        if not isinstance(other, (int, float)):
            raise TypeError(f"Unsupported type {type(other)} for addition")
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return True if self.km < other.km else False
        else:
            return True if self.km < other else False

    def __gt__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return True if self.km > other.km else False
        else:
            return True if self.km > other else False

    def __eq__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return True if self.km == other.km else False
        else:
            return True if self.km == other else False

    def __le__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return True if self.km <= other.km else False
        else:
            return True if self.km <= other else False

    def __ge__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return True if self.km >= other.km else False
        else:
            return True if self.km >= other else False
    pass
