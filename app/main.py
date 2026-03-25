# class Distance:
#     def __init__(self, km):
#         self.km = km
#
#     def __str__(self) -> str:
#         return f"Distance: {self.km} kilometers."
#
#     def __repr__(self) -> str:
#         return f"Distance(km={self.km})"
#
#     def __add__(self, other: Distance):
#         if isinstance(other, Distance):
#             amount_to_add = other.km
#         elif isinstance(other, (int, float)):
#             amount_to_add = other
#         else:
#             return NotImplemented
#         return Distance(self.km + amount_to_add)
#
#     def __iadd__(self, other):
#         if isinstance(other, Distance):
#             amount = other.km
#         elif isinstance(other, (int, float)):
#             amount = other
#         else:
#             return NotImplemented
#         self.km += amount
#         return self
#
#     def __mul__(self, other):
#         if isinstance(other, (int, float)):
#             return Distance(self.km * other)
#         return NotImplemented
#
#     def __truediv__(self, other):
#         if isinstance(other, (int, float)):
#             result = round(self.km / other, 2)
#             return Distance(result)
#
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, Distance):
#             return self.km < other.km
#         if isinstance(other, (int, float)):
#             return self.km < other
#         return NotImplemented
#
#     def __gt__(self, other):
#         if isinstance(other, Distance):
#             return self.km > other.km
#         if isinstance(other, (int, float)):
#             return self.km > other
#         return NotImplemented
#
#     def __le__(self, other):
#         if isinstance(other, Distance):
#             return self.km <= other.km
#         if isinstance(other, (int, float)):
#             return self.km <= other
#         return NotImplemented
#
#     def __ge__(self, other):
#         if isinstance(other, Distance):
#             return self.km >= other.km
#         if isinstance(other, (int, float)):
#             return self.km >= other
#         return NotImplemented
#
#     def __eq__(self, other):
#         if isinstance(other, Distance):
#             return self.km == other.km
#         if isinstance(other, (int, float)):
#             return self.km == other
#         return NotImplemented

from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km: int | float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            amount_to_add = other.km
        elif isinstance(other, (int, float)):
            amount_to_add = other
        else:
            return NotImplemented
        return Distance(self.km + amount_to_add)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            amount = other.km
        elif isinstance(other, (int, float)):
            amount = other
        else:
            return NotImplemented
        self.km += amount
        return self

    def __mul__(self, other: int | float) -> Distance | None:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            result = round(self.km / other, 2)
            return Distance(result)
        return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented
