def _convert_to_km(other: (int, float)) -> float:
    if isinstance(other, Distance):
        return other.km
    elif isinstance(other, (int, float)):
        return float(other)
    raise TypeError("Unsupported type for arithmetic operation")


class Distance:

    def __init__(self, km: float = 0.0) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (int, float)) -> "Distance":
        return Distance(self.km + _convert_to_km(other))

    def __iadd__(self, other: (int, float)) -> "Distance":
        self.km += _convert_to_km(other)
        return self

    def __mul__(self, other: (int, float)) -> "Distance":
        return Distance(self.km * _convert_to_km(float(other)))

    def __truediv__(self, other: (int, float)) -> "Distance":
        other_km = _convert_to_km(other)
        if other_km == 0:
            raise ValueError("Cannot divide by zero")
        return Distance(round(self.km / float(other), 2))

    def __lt__(self, other: (int, float)) -> bool:
        return self.km < _convert_to_km(other)

    def __gt__(self, other: (int, float)) -> bool:
        return self.km > _convert_to_km(other)

    def __eq__(self, other: (int, float)) -> bool:
        return self.km == _convert_to_km(other)

    def __le__(self, other: (int, float)) -> bool:
        return self.km <= _convert_to_km(other)

    def __ge__(self, other: (int, float)) -> bool:
        return self.km >= _convert_to_km(other)
