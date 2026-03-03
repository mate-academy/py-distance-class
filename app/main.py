class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float) -> float:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        result = self.km + value
        return Distance(result)

    def __iadd__(self, other: float) -> float:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        self.km = self.km + value
        return self

    def __mul__(self, other: float) -> float:
        if isinstance(other, Distance):
            raise TypeError
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> float:
        if isinstance(other, Distance):
            raise TypeError
        result = round(self.km / other, 2)
        return Distance(result)

    def __lt__(self, other: float) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km < value

    def __gt__(self, other: float) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km > value

    def __eq__(self, other: float) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km == value

    def __le__(self, other: float) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km <= value

    def __ge__(self, other: float) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km >= value
