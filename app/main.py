class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> object:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return Distance(self.km + value)

    def __iadd__(self, other) -> object:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        self.km = self.km + value
        return self

    def __mul__(self, other) -> object:
        if isinstance(other, Distance):
            return NotImplemented
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return Distance(self.km * value)

    def __truediv__(self, other) -> float:
        if isinstance(other, Distance):
            return NotImplemented
        elif isinstance(other, (int, float)) and other != 0:
            result = round(self.km / other, 2)
        else:
            return NotImplemented
        return Distance(result)

    def __lt__(self, other) -> object:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return self.km < value

    def __gt__(self, other) -> object:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return self.km > value

    def __eq__(self, other) -> object:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return self.km == value

    def __le__(self, other) -> object:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return self.km <= value

    def __ge__(self, other) -> object:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return self.km >= value