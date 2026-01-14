from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError("Can only add Distance objects or numbers")

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Can only add Distance objects or numbers")
        return self

    def __mul__(self, other: Union[int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError("Can only multiply Distance by numbers")

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            return Distance(round(self.km / other, 2))
        raise TypeError("Can only divide Distance by numbers")

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        raise TypeError("""
        Can only compare Distance
        with Distance objects or numbers
        """)

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        raise TypeError("""
        Can only
        compare Distance with
        Distance objects or numbers
        """)

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        raise TypeError("""
        Can only compare
        Distance with Distance
        objects or numbers
        """)

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        raise TypeError("""
        Can only compare
        Distance with Distance
        objects or numbers
        """)

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError("""
        Can only compare
        Distance with Distance
        objects or numbers
        """)
