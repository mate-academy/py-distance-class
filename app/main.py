from typing import Union


class Distance:

    def __init__(self, km: Union[int, float]) -> None:
        if not isinstance(km, (int, float)):
            raise TypeError(
                f"Expected int or float, got {type(km).__name__}"
            )
        else:
            self.km = km

    @staticmethod
    def check_other(other: Union["Distance", int, float]) -> Union[int, float]:
        if not isinstance(other, (Distance, int, float)):
            raise TypeError(
                f"Expected Distance, int or float, got {type(other).__name__}"
            )
        if isinstance(other, Distance):
            return other.km
        else:
            return other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        other = self.check_other(other)
        return Distance(self.km + other)

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        other = self.check_other(other)
        self.km += other
        return self

    def __mul__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError(
                "Method __mul__ will not accept Distance attributes"
            )
        other = self.check_other(other)
        return Distance(self.km * other)

    def __truediv__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError(
                "Method __truediv__ will not accept Distance attributes"
            )
        other = self.check_other(other)
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        other = self.check_other(other)
        return self.km < other

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        other = self.check_other(other)
        return self.km > other

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        other = self.check_other(other)
        return self.km == other

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        other = self.check_other(other)
        return self.km <= other

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        other = self.check_other(other)
        return self.km >= other

    def __ne__(self, other: Union["Distance", int, float]) -> bool:
        other = self.check_other(other)
        return self.km != other
