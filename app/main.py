class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | int | float") -> "Distance":
        value = other.km if isinstance(other, Distance) else other
        return Distance(self.km + value)

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float) -> "Distance":
        new_km = self.km * other
        return Distance(new_km)

    def __truediv__(self, other: int | float) -> "Distance":
        if other == 0:
            raise ZeroDivisionError
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km < value

    def __gt__(self, other: int | float | Distance) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km > value

    def __eq__(self, other: int | float | Distance) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km == value

    def __le__(self, other: int | float | Distance) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km <= value

    def __ge__(self, other: int | float | Distance) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km >= value
