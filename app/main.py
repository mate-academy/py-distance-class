from typing import Union


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, (int, float)):
            self.km = self + other
        else:
            self.km += other.km
        return self

    def __mul__(self, number: Union[int, float]) -> "Distance":
        return Distance(self.km * number)

    def __truediv__(self, number: Union[int, float]) -> "Distance":
        return Distance(round(self.km / number, 2))

    def __lt__(self, number: Union[int, float]) -> bool:
        inst = Distance(number)
        return self.km < inst.km

    def __gt__(self, number: Union[int, float]) -> bool:
        inst = Distance(number)
        return self.km > inst.km

    def __eq__(self, number: Union[int, float]) -> bool:
        inst = Distance(number)
        return self.km == inst.km

    def __le__(self, number: Union[int, float]) -> bool:
        inst = Distance(number)
        return self.km <= inst.km

    def __ge__(self, number: Union[int, float]) -> bool:
        inst = Distance(number)
        return self.km >= inst.km

    def __len__(self) -> object:
        return self.km
