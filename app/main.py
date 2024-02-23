from typing import Union


class Distance:
    # Write your code here
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, "Distance"]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Union[int, "Distance"]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, number: int) -> "Distance":
        return Distance(self.km * number)

    def __truediv__(self, number: int) -> "Distance":
        return Distance(round(self.km / number, 2))

    def __lt__(self, number: int) -> bool:
        return self.km < number

    def __gt__(self, number: int) -> bool:
        return self.km > number

    def __eq__(self, number: int) -> bool:
        return self.km == number

    def __le__(self, number: int) -> bool:
        return self.km <= number

    def __ge__(self, number: int) -> bool:
        return self.km >= number
