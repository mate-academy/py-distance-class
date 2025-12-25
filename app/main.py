from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other_distance: Distance | int | float) -> Distance:
        if isinstance(other_distance, Distance):
            return Distance(self.km + other_distance.km)
        elif isinstance(other_distance, (int, float)):
            return Distance(self.km + other_distance)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +: "
                f"'Distance' and {type(other_distance)}")

    def __iadd__(self, other_distance: Distance | int | float) -> Distance:
        if isinstance(other_distance, Distance):
            self.km += other_distance.km
        elif isinstance(other_distance, (int, float)):
            self.km += other_distance
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +: "
                f"'Distance' and {type(other_distance)}")

        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance) and self.km < other.km:
            return True
        if isinstance(other, (int, float)) and self.km < other:
            return True

        return False

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance) and self.km > other.km:
            return True
        if isinstance(other, (int, float)) and self.km > other:
            return True

        return False

    def __eq__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance) and self.km == other.km:
            return True
        if isinstance(other, (int, float)) and self.km == other:
            return True

        return False

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance) and self.km <= other.km:
            return True
        if isinstance(other, (int, float)) and self.km <= other:
            return True

        return False

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance) and self.km >= other.km:
            return True
        if isinstance(other, (int, float)) and self.km >= other:
            return True

        return False
