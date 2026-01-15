from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        return f"Distance: {self._format(self.km)} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self._format(self.km)})"

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: Union[int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero.")
            result = round(self.km / other, 2)
            return Distance(result)
        return NotImplemented

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented

    @staticmethod
    def _format(value: float) -> str:
        formatted = format(value, ".2f")
        if "." in formatted:
            formatted = formatted.rstrip("0").rstrip(".")
        return formatted
