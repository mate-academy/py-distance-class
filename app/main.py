from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __add__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(km=self.km + other)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +: "
                f"'Distance' and '{type(other).__name__}'")

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __iadd__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +=: "
                f"'Distance' and '{type(other).__name__}'")
        return self

    def __mul__(self, number: float) -> Distance:
        return Distance(km=self.km * number)

    def __truediv__(self, number: float) -> Distance:

        return Distance(km=round(self.km / number, 2))

    def __eq__(self, number: float) -> bool:
        return self.km == number

    def __gt__(self, number: float) -> bool:
        return self.km > number

    def __lt__(self, number: float) -> bool:
        return self.km < number

    def __le__(self, number: float) -> bool:
        return self.km <= number

    def __ge__(self, number: float) -> bool:
        return self.km >= number
