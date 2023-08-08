from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", float, int]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise ValueError("Unsupported operand type for +")

    def __iadd__(self, other: Union["Distance", float, int]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise ValueError("Unsupported operand type for +=")
        return self

    def __mul__(self, other: Union[float, int]) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError("Unsupported operand type for *")
        elif isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise ValueError("Unsupported operand type for *")

    def __truediv__(self, other: Union[float, int]) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError("Unsupported operand type for /")
        elif isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise ValueError("Unsupported operand type for /")

    def __lt__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise ValueError("Unsupported operand type for <")

    def __gt__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise ValueError("Unsupported operand type for >")

    def __eq__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise ValueError("Unsupported operand type for ==")

    def __le__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise ValueError("Unsupported operand type for <=")

    def __ge__(self, other: Union["Distance", float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise ValueError("Unsupported operand type for >=")
