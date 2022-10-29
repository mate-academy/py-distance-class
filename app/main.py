from typing import Union


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __add__(self, other: Union[int, float]) -> Union:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __repr__(self) -> str:
        return "Distance(km=" + str(self.km) + ")"

    def __str__(self) -> str:
        return "Distance: " + str(self.km) + " kilometers."

    def __lt__(self, other: Union[int, float]) -> bool:
        return self.km < other

    def __gt__(self, other: Union[int, float]) -> bool:
        return self.km > other

    def __eq__(self, other: Union[int, float]) -> bool:
        return self.km == other

    def __le__(self, other: Union[int, float]) -> bool:
        return self.km <= other

    def __ge__(self, other: Union[int, float]) -> bool:
        return self.km >= other

    def __iadd__(self, other: Union[int, float]) -> Union:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self

    def __mul__(self, other: Union[int, float]) -> Union:
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> float:
        return Distance(round(self.km / other, 2))

    def __len__(self) -> Union:
        return self.km
