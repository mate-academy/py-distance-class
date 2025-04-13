from typing import Union, Any


class Distance:
    def __init__(self, km: float) -> None:
        if km < 0:
            raise ValueError("Distance cannot be negative")
        self.km: float = float(km)

    def __str__(self) -> str:
        km_str = str(int(self.km)) if self.km.is_integer() else str(self.km)
        return f"Distance: {km_str} kilometers."

    def __repr__(self) -> str:
        km_str = str(int(self.km)) if self.km.is_integer() else str(self.km)
        return f"Distance(km={km_str})"

    def __add__(self, other: Union["Distance", float, int]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: Union["Distance", float, int]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, number: Union[float, int]) -> "Distance":
        if isinstance(number, (int, float)):
            return Distance(self.km * number)
        return NotImplemented

    def __truediv__(self, number: Union[float, int]) -> "Distance":
        if isinstance(number, (int, float)):
            if number == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = self.km / number
            return Distance(round(result, 2))
        return NotImplemented

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
