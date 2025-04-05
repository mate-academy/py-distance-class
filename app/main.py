from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            new_ds = Distance(self.km + other.km)
            return new_ds
        elif isinstance(other, (int, float)):
            new_ds = Distance(self.km + other)
            return new_ds
        else:
            raise ValueError(f"Unsupported type {other} - {type(other)} ")

    def __iadd__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            raise ValueError(f"Unsupported type {other} - {type(other)} ")

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            raise TypeError("Cannot divide two Distance objects")
        elif isinstance(other, (int, float)):
            new_ds = Distance(self.km * other)
            return new_ds
        else:
            raise ValueError(f"Unsupported type {other} - {type(other)} ")

    def __truediv__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            raise TypeError("Cannot divide two Distance objects")
        elif isinstance(other, (int, float)):
            new_ds = Distance(round(self.km / other, 2))
            return new_ds
        else:
            raise ValueError(f"Unsupported type {other} - {type(other)} ")

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise ValueError(f"Unsupported type {other} - {type(other)} ")

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise ValueError(f"Unsupported type {other} - {type(other)} ")

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise False

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise ValueError(f"Unsupported type {other} - {type(other)} ")

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise ValueError(f"Unsupported type {other} - {type(other)} ")
