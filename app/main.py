class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __eq__(self, value: Distance | int | float) -> bool:
        if isinstance(value, Distance):
            return self.km == value.km
        return self.km == value

    def __gt__(self, value: Distance | int | float) -> bool:
        if isinstance(value, Distance):
            return self.km > value.km
        return self.km > value

    def __ge__(self, value: Distance | int | float) -> bool:
        if isinstance(value, Distance):
            return self.km >= value.km
        return self.km >= value

    def __lt__(self, value: Distance | int | float) -> bool:
        if isinstance(value, Distance):
            return self.km < value.km
        return self.km < value

    def __le__(self, value: Distance | int | float) -> bool:
        if isinstance(value, Distance):
            return self.km <= value.km
        return self.km <= value
