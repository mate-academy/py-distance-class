from __future__ import annotations


class Distance:
    def __init__(self, kilometers: int) -> None:
        self.km = kilometers

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, new_distance: Distance | int | float) -> Distance:
        if isinstance(new_distance, (int, float)):
            return Distance(self.km + new_distance)
        return Distance(self.km + new_distance.km)

    def __iadd__(self, new_distance: Distance | int | float) -> Distance:
        if isinstance(new_distance, (int, float)):
            self.km += new_distance
        else:
            self.km += new_distance.km
        return self

    def __mul__(self, number: int | float) -> Distance:
        return Distance(self.km * number)

    def __truediv__(self, number: int | float) -> Distance:
        return Distance(round(self.km / number, 2))

    def __lt__(self, distance: int | float) -> bool:
        if isinstance(distance, (int, float)):
            return self.km < distance
        return self.km < distance.km

    def __gt__(self, distance: int | float) -> bool:
        if isinstance(distance, (int, float)):
            return self.km > distance
        return self.km > distance.km

    def __eq__(self, distance: int | float) -> bool:
        if isinstance(distance, (int, float)):
            return self.km == distance
        return self.km == distance.km

    def __le__(self, distance: int | float) -> bool:
        if isinstance(distance, (int, float)):
            return self.km <= distance
        return self.km <= distance.km

    def __ge__(self, distance: int | float) -> bool:
        if isinstance(distance, (int, float)):
            return self.km >= distance
        return self.km >= distance.km
