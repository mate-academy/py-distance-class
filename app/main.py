from typing import Union


class Distance:
    # Write your code here
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        try:
            return Distance(self.km + other.km)
        except AttributeError:
            return Distance(self.km + other)

    def __len__(self):
        try:
            return len(self.km)
        except TypeError:
            return self.km

    def __mul__(self, other):
        try:
            return Distance(self.km * other.km)
        except AttributeError:
            return Distance(self.km * other)

    def __truediv__(self, other):
        try:
            return Distance(self.km / other.km)
        except AttributeError:
            return Distance(self.km / other)

    def __eq__(self, other):
        try:
            return self.km == other.km
        except AttributeError:
            return self.km == other

    def __gt__(self, other):
        try:
            return self.km > other.km
        except AttributeError:
            return self.km > other

    def __lt__(self, other):
        try:
            return self.km < other.km
        except AttributeError:
            return self.km < other

    def __ge__(self, other):
        try:
            return self.km >= other.km
        except AttributeError:
            return self.km >= other

    def __le__(self, other):
        try:
            return self.km <= other.km
        except AttributeError:
            return self.km <= other

