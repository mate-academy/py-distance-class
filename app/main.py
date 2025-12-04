class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def get_value(self, other: "Distance | int | float") -> \
            "int | float | NotImplemented":
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __add__(self, other: "Distance | int | float") -> "Distance":
        value = self.get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return Distance(self.km + value)

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        value = self.get_value(other)
        if value is NotImplemented:
            return NotImplemented
        self.km += value
        return self

    def __mul__(self, other: "int | float") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: "int | float") -> "Distance":
        if isinstance(other, (int, float)) and other != 0:
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __lt__(self, other: "Distance | int | float") -> bool:
        value = self.get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km < value

    def __gt__(self, other: "Distance | int | float") -> bool:
        value = self.get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km > value

    def __le__(self, other: "Distance | int | float") -> bool:
        value = self.get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km <= value

    def __ge__(self, other: "Distance | int | float") -> bool:
        value = self.get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km >= value

    def __eq__(self, other: "Distance | int | float") -> bool:
        value = self.get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km == value
