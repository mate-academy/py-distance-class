from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, number: any) -> float:
        if isinstance(number, Distance):
            return Distance(self.km + number.km)
        else:
            distance = Distance(number)
            return Distance(self.km + distance.km)

    def __iadd__(self, number: any) -> float:
        if isinstance(number, Distance):
            self.km += number.km
            return self
        else:
            distance = Distance(number)
            self.km += distance.km
            return self

    def __mul__(self, number: int) -> float:
        return Distance(self.km * number)

    def __truediv__(self, number: int) -> float:
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
