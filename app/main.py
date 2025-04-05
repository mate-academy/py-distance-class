from typing import Union, Optional, TypeVar

Tp = TypeVar("Tp", bound="Distance")


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Union[Tp, int, float]) -> Tp:
        if isinstance(other, Distance):
            new_ds = Distance(self.km + other.km)
            return new_ds
        elif isinstance(other, (int, float)):
            new_ds = Distance(self.km + other)
            return new_ds
        raise ValueError(f"Unsupported type {other} - {type(other)} ")

    def __iadd__(self, other: Union[Tp, int, float]) -> Tp:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self
        raise ValueError(f"Unsupported type {other} - {type(other)} ")

    def __mul__(self, other: Union[Tp, int, float]) -> Optional[Tp]:
        if isinstance(other, Distance):
            raise TypeError("Cannot divide two Distance objects")
        elif isinstance(other, (int, float)):
            new_ds = Distance(self.km * other)
            return new_ds
        raise ValueError(f"Unsupported type {other} - {type(other)} ")

    def __truediv__(self, other: Union[Tp, int, float]) -> Optional[Tp]:
        if isinstance(other, Distance):
            raise TypeError("Cannot divide two Distance objects")
        elif isinstance(other, (int, float)):
            new_ds = Distance(round(self.km / other, 2))
            return new_ds
        raise ValueError(f"Unsupported type {other} - {type(other)} ")

    def __lt__(self, other: Union[Tp, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        raise ValueError(f"Unsupported type {other} - {type(other)} ")

    def __gt__(self, other: Union[Tp, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        raise ValueError(f"Unsupported type {other} - {type(other)} ")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        raise False

    def __le__(self, other: Union[Tp, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        raise ValueError(f"Unsupported type {other} - {type(other)} ")

    def __ge__(self, other: Union[Tp, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        raise ValueError(f"Unsupported type {other} - {type(other)} ")
