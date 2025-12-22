class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def get_value(self, other: iint | float | Distance) -> float:
        if isinstance(other, Distance):
            return other.km
        return other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, value: int | float | Distance) -> Distance:
        return Distance(self.km * value)

    def __truediv__(self, value: int | float | Distance) -> Distance:
        return Distance(round(self.km / value, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        return self.km < self.get_value(other)

    def __le__(self, other: int | float | Distance) -> bool:
        return self.km <= self.get_value(other)

    def __gt__(self, other: int | float | Distance) -> bool:
        return self.km > self.get_value(other)

    def __ge__(self, other: int | float | Distance) -> bool:
        return self.km >= self.get_value(other)

    def __eq__(self, other: int | float | Distance) -> bool:
        return self.km == self.get_value(other)
