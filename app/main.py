from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError("Addition only supported for\n"
                        "Distance or numeric types.")

    def __iadd__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Addition only supported for\n"
                            "Distance or numeric types.")
        return self

    def __mul__(self, factor: Any) -> "Distance":
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)
        raise TypeError("Multiplication only supported with numeric types.")

    def __truediv__(self, divisor: Any) -> "Distance":
        if isinstance(divisor, (int, float)) and divisor != 0:
            return Distance(round(self.km // divisor, 2))
        raise TypeError("Division only supported with non-zero numeric types.")

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        raise TypeError("Comparison only supported for\n"
                        "Distance or numeric types.")

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        raise TypeError("Comparison only supported for\n"
                        "Distance or numeric types.")

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        raise TypeError("Equality comparison only supported for\n"
                        "Distance or numeric types.")

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other
        raise TypeError("Comparison only supported for\n"
                        "Distance or numeric types.")

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError("Comparison only supported for\n"
                        "Distance or numeric types.")
