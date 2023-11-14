from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"{Distance.__name__}: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"{Distance.__name__}(km={self.km})"

    def __add__(self, other: Union["Distance", int, float]
                ) -> Union["Distance", TypeError]:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError(
                f"{other} must be {Distance.__name__} or (int, float)")

    def __iadd__(self, other: Union["Distance", int, float]
                 ) -> Union[None, TypeError]:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            raise TypeError(
                f"{other} must be {Distance.__name__} or (int, float)")

    def __mul__(self, other: int | float) -> Union["Distance", TypeError]:
        if isinstance(other, Distance):
            raise TypeError(
                f"{other} must be {Distance.__name__} or (int, float)")
        else:
            return Distance(self.km * other)

    def __truediv__(self, other: Union["Distance", int, float]
                    ) -> Union["Distance", TypeError]:
        if isinstance(other, Distance):
            raise TypeError(
                f"{other} must be {Distance.__name__} or (int, float)")
        return Distance(round((self.km / other), 2))

    def __lt__(self, other: Union["Distance", int, float]
               ) -> Union["Distance", TypeError]:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError(
                f"{other} must be {Distance.__name__} or (int, float)")

    def __gt__(self, other: Union["Distance", int, float]
               ) -> Union["Distance", TypeError]:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError(
                f"{other} must be {Distance.__name__} or (int, float)")

    def __eq__(self, other: Union["Distance", int, float]
               ) -> Union["Distance", TypeError]:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError(
                f"{other} must be {Distance.__name__} or (int, float)")

    def __le__(self, other: Union["Distance", int, float]
               ) -> Union["Distance", TypeError]:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError(
                f"{other} must be {Distance.__name__} or (int, float)")

    def __ge__(self, other: Union["Distance", int, float]
               ) -> Union["Distance", TypeError]:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError(
                f"{other} must be {Distance.__name__} or (int, float)")
