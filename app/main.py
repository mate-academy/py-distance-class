from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError(
            f"Argument 'other' must be of type"
            f"{self.__class__.__name__}, int, float"
            f"not {type(other).__name__}"
        )

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        raise TypeError(
            f"Argument 'other' must be of type"
            f"{self.__class__.__name__}, int, float"
            f"not {type(other).__name__}"
        )

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError(
            f"Argument 'other' must be of type"
            f"int, float not {type(other).__name__}"
        )

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        raise TypeError(
            f"Argument 'other' must be of type"
            f"int, float not {type(other).__name__}"
        )

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        raise TypeError(
            f"Argument 'other' must be of type"
            f"{self.__class__.__name__}, int, float"
            f"not {type(other).__name__}"
        )

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        raise TypeError(
            f"Argument 'other' must be of type"
            f"{self.__class__.__name__}, int, float"
            f"not {type(other).__name__}"
        )

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        raise TypeError(
            f"Argument 'other' must be of type"
            f"{self.__class__.__name__}, int, float"
            f"not {type(other).__name__}"
        )

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other
        raise TypeError(
            f"Argument 'other' must be of type"
            f"{self.__class__.__name__}, int, float"
            f"not {type(other).__name__}"
        )

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError(
            f"Argument 'other' must be of type"
            f"{self.__class__.__name__}, int, float"
            f"not {type(other).__name__}"
        )
