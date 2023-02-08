from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, number: int | float) -> Distance:
        if isinstance(number, Distance):
            return Distance(km=self.km + number.km)
        else:
            number = Distance(number)
            return Distance(km=self.km + number.km)

    def __iadd__(self, number: int | float) -> Distance:
        if isinstance(number, Distance):
            self.km += number.km
            return self
        else:
            number = Distance(number)
            self.km += number.km
            return self

    def __mul__(self, number: int | float) -> Distance:
        return Distance(self.km * number)

    def __truediv__(self, number: int | float) -> Distance:
        return Distance(km=round((self.km / number), 2))

    def __lt__(self, number: int | float) -> bool:
        return self.km < number

    def __gt__(self, number: int | float) -> bool:
        return self.km > number

    def __eq__(self, number: int | float) -> bool:
        return self.km == number

    def __le__(self, number: int | float) -> bool:
        return self.km <= number

    def __ge__(self, number: int | float) -> bool:
        return self.km >= number
