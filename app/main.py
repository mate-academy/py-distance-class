class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def _get_value(value: "Distance | int | float") -> int | float:
        if isinstance(value, Distance):
            return value.km
        if isinstance(value, (int, float)):
            return value
        raise TypeError(f"Unsupported type: {type(value).__name__}")

    def __add__(self, other: "Distance | int | float") -> "Distance":
        return Distance(self.km + self._get_value(other))

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        self.km += self._get_value(other)
        return self

    def __mul__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError(f"Cannot multiply Distance by {type(other).__name__}")

    def __truediv__(self, division: int | float) -> "Distance":
        if isinstance(division, (int, float)):
            if division == 0:
                raise ZeroDivisionError("division by zero")
            return Distance(round(self.km / division, 2))
        raise TypeError(f"Cannot divide Distance by {type(division).__name__}")

    def __lt__(self, other: "Distance | int | float") -> bool:
        return self.km < self._get_value(other)

    def __gt__(self, other: "Distance | int | float") -> bool:
        return self.km > self._get_value(other)

    def __eq__(self, other: object) -> bool:
        try:
            return self.km == self._get_value(other)
        except TypeError:
            return False

    def __le__(self, other: "Distance | int | float") -> bool:
        return self.km <= self._get_value(other)

    def __ge__(self, other: "Distance | int | float") -> bool:
        return self.km >= self._get_value(other)
