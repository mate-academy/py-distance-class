from __future__ import annotations

class Distance:

    def __init__(self, km: int):
        self.km = km

    @staticmethod
    def other_validation(other):
        if isinstance(other, Distance):
            return other.km
        return other

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        return Distance(
            km=self.km + Distance.other_validation(other)
        )

    def __iadd__(self, other):
        self.km += Distance.other_validation(other)
        return self

    def __mul__(self, other):
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other):
        return Distance(
            km=round(self.km / other, 2)
        )

    def __lt__(self, other):
        if self.km < Distance.other_validation(other):
            return True
        return False

    def __gt__(self, other):
        if self.km > Distance.other_validation(other):
            return True
        return False

    def __eq__(self, other):
        if self.km == Distance.other_validation(other):
            return True
        return False

    def __le__(self, other):
        if self.km <= Distance.other_validation(other):
            return True
        return False

    def __ge__(self, other):
        if self.km >= Distance.other_validation(other):
            return True
        return False
