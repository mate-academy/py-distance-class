
class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def _value(other: object) -> int | float | None:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return None

    def __add__(self, other: "Distance | int | float") -> "Distance":
        value = self._value(other)
        if value is None:
            return NotImplemented
        return Distance(self.km + value)

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        value = self._value(other)
        if value is None:
            return NotImplemented
        self.km += value
        return self

    def __mul__(self, other: int | float) -> "Distance":
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> "Distance":
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: "Distance | int | float") -> bool:
        value = self._value(other)
        if value is None:
            return NotImplemented
        return self.km < value

    def __gt__(self, other: "Distance | int | float") -> bool:
        value = self._value(other)
        if value is None:
            return NotImplemented
        return self.km > value

    def __le__(self, other: "Distance | int | float") -> bool:
        value = self._value(other)
        if value is None:
            return NotImplemented
        return self.km <= value

    def __ge__(self, other: "Distance | int | float") -> bool:
        value = self._value(other)
        if value is None:
            return NotImplemented
        return self.km >= value

    def __eq__(self, other: object) -> bool:
        value = self._value(other)
        if value is None:
            return NotImplemented
        return self.km == value