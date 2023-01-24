from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, distance: int) -> Distance:
        if isinstance(distance, Distance):
            distance3 = Distance(distance.km + self.km)
        else:
            distance3 = Distance(distance + self.km)
        return distance3

    def __iadd__(self, distance: int) -> Distance:
        if isinstance(distance, Distance):
            self.km = distance.km + self.km
        else:
            self.km = distance + self.km
        return self

    def __mul__(self, number: float) -> Distance:
        self.km = self.km * number
        return self

    def __truediv__(self, number: float) -> Distance:
        self.km = round(self.km / number, 2)
        return self

    def __lt__(self, distance: int) -> bool:
        if isinstance(distance, Distance):
            if self.km < distance.km:
                return True
            return False
        if self.km < distance:
            return True
        return False

    def __gt__(self, distance: int) -> bool:
        if isinstance(distance, Distance):
            if self.km > distance.km:
                return True
            return False
        if self.km > distance:
            return True
        return False

    def __eq__(self, distance: int) -> bool:
        if isinstance(distance, Distance):
            if self.km == distance.km:
                return True
            return False
        if self.km == distance:
            return True
        return False

    def __le__(self, distance: int) -> bool:
        if isinstance(distance, Distance):
            if self.km <= distance.km:
                return True
            return False
        if self.km <= distance:
            return True
        return False

    def __ge__(self, distance: int) -> bool:
        if isinstance(distance, Distance):
            if self.km >= distance.km:
                return True
            return False
        if self.km >= distance:
            return True
        return False

    def __round__(self, end: int) -> float:
        return round(self.km, end)
