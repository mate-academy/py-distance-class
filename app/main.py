from __future__ import  annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def func_for_math(self, other: Distance | int, decimal: str) -> Distance:
        result = 0
        if isinstance(other, Distance):
            if decimal == "+":
                result = self.km + other.km
            if decimal == "+=":
                self.km += other.km
                return self
            return Distance(
                km=result
            )
        else:
            if decimal == "+":
                result = self.km + other
            if decimal == "+=":
                self.km += other
                return self
        return Distance(
            km=result
        )

    def funct_for_mult_div(self, other, decimal) -> Distance:
        result = 0
        if decimal == "*":
            result = self.km * other
        if decimal == "/":
            result = round(self.km / other, 2)
        return Distance(
            km=result
        )

    def func_for_leveling(self, other: Distance | int, decimal: str) -> bool:
        if isinstance(other, Distance):
            if decimal == "<":
                return self.km < other.km
            if decimal == "<=":
                return self.km <= other.km
            if decimal == ">":
                return self.km > other.km
            if decimal == ">=":
                return self.km >= other.km
            if decimal == "==":
                return self.km == other.km
        else:
            if decimal == "<":
                return self.km < other
            if decimal == "<=":
                return self.km <= other
            if decimal == ">":
                return self.km > other
            if decimal == ">=":
                return self.km >= other
            if decimal == "==":
                return self.km == other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | Distance) -> Distance:
        return self.func_for_math(other, "+")

    def __iadd__(self, other: int | Distance) -> Distance:
        return self.func_for_math(other, "+=")

    def __mul__(self, other: int) -> Distance:
        return self.funct_for_mult_div(other, "*")

    def __truediv__(self, other: int) -> Distance:
        return self.funct_for_mult_div(other, "/")

    def __lt__(self, other) -> bool:
        return self.func_for_leveling(other, "<")

    def __le__(self, other) -> bool:
        return self.func_for_leveling(other, "<=")

    def __gt__(self, other) -> bool:
        return self.func_for_leveling(other, ">")

    def __ge__(self, other) -> bool:
        return self.func_for_leveling(other, ">=")

    def __eq__(self, other) -> bool:
        return self.func_for_leveling(other, "==")
