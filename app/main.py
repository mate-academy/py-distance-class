from typing import Union


class Distance:
    # Write your code here
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise False

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise
        return self

    def __mul__(self, other: Union[int, float]) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> "Distance" or None:
        if isinstance(other, (int, float)):
            if other == 0:
                return None
            result = self.km / other
            return Distance(round(result, 2))
        else:
            return None

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            if self.km < other.km:
                return True
        elif isinstance(other, (int, float)):
            if self.km < other:
                return True
        return False

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            if self.km > other.km:
                return True
        elif isinstance(other, (int, float)):
            if self.km > other:
                return True
        return False

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            if self.km == other.km:
                return True
        elif isinstance(other, (int, float)):
            if self.km == other:
                return True
        return False

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            if self.km <= other.km:
                return True
        elif isinstance(other, (int, float)):
            if self.km <= other:
                return True
        return False

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            if self.km >= other.km:
                return True
        elif isinstance(other, (int, float)):
            if self.km >= other:
                return True
        return False
